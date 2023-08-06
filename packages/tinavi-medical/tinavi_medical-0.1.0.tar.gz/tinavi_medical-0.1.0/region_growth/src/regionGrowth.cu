#include <cuda.h>
#include <cuda_runtime_api.h>
#include <dirent.h>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

using namespace std;

#define CUDA_SAFE_CALL(x)                                                         \
{                                                                               \
	if (x != cudaSuccess)                                                         \
	{                                                                             \
		printf("  Cuda error %i occured in %s, line %i!\n", x, __FILE__, __LINE__); \
		printf("  Cuda error message:  %s\n", cudaGetErrorString(x));               \
		char buffer[256];                                                           \
		cin >> buffer;                                                              \
		exit(-1);                                                                   \
	}                                                                             \
}

typedef unsigned char uchar;

const int size_uchar = sizeof(uchar);

__device__ bool IsNeighborForDistanceTransform(cudaSurfaceObject_t track_surf, int _x, int _y, int _z, int depth, int width, int height, int iterations)
{
	bool tag = false;
	uchar track_data;
	surf3Dread(&track_data, track_surf, _x, _y, _z, cudaBoundaryModeTrap);
	// track_data = tex3D(text_track_ref, _x, _y, _z);
	if (track_data <= iterations)
	{
		return tag;
	}

	for (int k = _z - 1; k <= _z + 1; k++)
	{
		for (int j = _y - 1; j <= _y + 1; j++)
		{
			for (int i = _x - 1; i <= _x + 1; i++)
			{
				if (((k > 0) && (k < depth)) && ((j > 0) && (j < height)) && ((i > 0) && (i < width)))
				{
					// if (((i+k)-(x+z))*((i+k)-(x+z))!=1) continue;
					// if (((j+k)-(j+z))*((j+k)-(y+z))!=1) continue;
					// int index_neighbor = GetFlat(i, j, k, width, height);
					// if (index_neighbor != index)
					if (i != _x || j != _y || k != _z)
					{
						unsigned char neighbor_value;
						surf3Dread(&neighbor_value, track_surf, i, j, k, cudaBoundaryModeTrap);
						// neighbor_value = tex3D(text_track_ref, i, j, k);
						if ((neighbor_value == iterations) && track_data > iterations)
						{
							tag = true;
							return tag;
						}
					}
				}
			}
		}
	}
	return tag;
}

__global__ void DistanceTransform(cudaSurfaceObject_t track_surf, int *incluidos, int depth, int width, int height, int iterations)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;
	int z = blockIdx.z * blockDim.z + threadIdx.z;
	if ((x < width) && (y < height) && (z < depth))
	{
		// int i = GetFlat(x, y, z, width, height);
		bool tag = IsNeighborForDistanceTransform(track_surf, x, y, z, depth, width, height, iterations);
		__syncthreads();
		if (tag)
		{
			// track_data[i] = iterations + 1;
			unsigned char tmp_v = iterations + 1;
			if (tmp_v > 254)
			{
				printf("tmp_v:  %d", tmp_v);
			}
			surf3Dwrite(tmp_v, track_surf, x * size_uchar, y, z, cudaBoundaryModeTrap);
			*incluidos += 1;
		}
	}
}

__global__ void InitWithLimits(cudaSurfaceObject_t track_surf_w, int iteration_limit, int lower_threshold, int upper_threshold, int depth, int width, int height)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;
	int z = blockIdx.z * blockDim.z + threadIdx.z;

	if ((x < width) && (y < height) && (z < depth))
	{
		// int i = GetFlat(x, y, z, width, height);
		unsigned char track_data;
		surf3Dread(&track_data, track_surf_w, x * size_uchar, y, z, cudaBoundaryModeTrap);
		// track_data = tex3D(text_track_ref, x, y, z);
		if (track_data >= lower_threshold && track_data < upper_threshold)
		{
	  		// track_data[i] = iteration_limit;
			surf3Dwrite(uchar(iteration_limit), track_surf_w, x * size_uchar, y, z, cudaBoundaryModeTrap);
		}
		else
		{
			// track_data[i] = 0;
			surf3Dwrite(uchar(0), track_surf_w, x * size_uchar, y, z, cudaBoundaryModeTrap);
		}
	}
}

__global__ void RefactorSeedData(cudaSurfaceObject_t tmp_surf, cudaSurfaceObject_t seed_surf, int depth, int width, int height)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;
	int z = blockIdx.z * blockDim.z + threadIdx.z;
	if (x >= width || y >= height || z >= depth)
	{
		return;
	}

	// int i = GetFlat(x, y, z, width, height);
	// uchar tmp_data_v = tex3D(text_tmp_ref, x, y, z);
	uchar tmp_data_v;
	surf3Dread(&tmp_data_v, tmp_surf, x * size_uchar, y, z);
	if (tmp_data_v > 0)
	{
		// seed_data[i] = tmp_data_v;
		surf3Dwrite(tmp_data_v, seed_surf, x, y, z);
	}
}

__device__ int IsNeighbor(cudaSurfaceObject_t seed_surf, int _x, int _y, int _z, int depth, int width, int height)
{
	uchar max_index = 0;

	// GetCoord(index, &x, &y, &z, width, height);

	for (int k = _z - 1; k <= _z + 1; k++)
	{
		for (int j = _y - 1; j <= _y + 1; j++)
		{
			for (int i = _x - 1; i <= _x + 1; i++)
			{
				if (((k > 0) && (k < depth)) && ((j > 0) && (j < height)) && ((i > 0) && (i < width)))
				{
					// int index_neighbor = GetFlat(i, j, k, width, height);
					// if (index_neighbor != index)
					if (i != _x || j != _y || k != _z)
					{
						// uchar seed_data_v = tex3D(text_seed_ref, i, j, k);
						uchar seed_data_v;
						surf3Dread(&seed_data_v, seed_surf, i, j, k);
						if (seed_data_v > 0)
						{
							return seed_data_v;
						}
					}
				}
			}
		}
	}
	return max_index;
}

__global__ void RegionGrowing(cudaSurfaceObject_t tmp_surf, cudaSurfaceObject_t seed_surf, cudaSurfaceObject_t track_surf_obj, int *incluidos, int depth, int width, int height, int growth_bound)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;
	int z = blockIdx.z * blockDim.z + threadIdx.z;
	if ((x < width) && (y < height) && (z < depth))
	{
		// int i = GetFlat(x, y, z, width, height);
		// uchar seed_data = tex3D(text_seed_ref, x, y, z);
		uchar seed_data;
		surf3Dread(&seed_data, seed_surf, x, y, z);
		if (seed_data != 0)
		{
			return;
		}

		uchar max_index = IsNeighbor(seed_surf, x, y, z, depth, width, height);
		__syncthreads();
		if (max_index > 0)
		{
			uchar tmp_v;
			surf3Dread(&tmp_v, track_surf_obj, x, y, z);
			// if (tex3D(text_track_ref, x, y, z) >= growth_bound)
			if (tmp_v >= growth_bound)
			{
				// tmp_data[i] = max_index;
				surf3Dwrite(max_index, tmp_surf, x * size_uchar, y, z);
				atomicAdd(incluidos, 1);
			}
		}
	}
}

extern "C"
{

	void RegionGrowthEntrance(uchar *h_track_data, uchar *h_seed_data, int width, int height, int depth, int lower_threshold, int upper_threshold, int distance_iteration_limit, int growth_iteration_limit, int gpu)
	{
		cudaSetDevice(gpu);
		size_t size_int = sizeof(int);

		// 开辟 GPU 内存: cuda_Array: track
		cudaChannelFormatDesc channelDesc = cudaCreateChannelDesc(8, 0, 0, 0, cudaChannelFormatKindUnsigned);
		cudaArray *d_track_array;
		cudaExtent extent3D;
		extent3D.width = width;
		extent3D.depth = depth;
		extent3D.height = height;
		CUDA_SAFE_CALL(cudaMalloc3DArray((cudaArray **)&d_track_array, &channelDesc, extent3D, cudaArraySurfaceLoadStore));

		// 开辟 GPU 内存: cuda_Array: tmp
		cudaArray *d_tmp_array;
		CUDA_SAFE_CALL(cudaMalloc3DArray((cudaArray **)&d_tmp_array, &channelDesc, extent3D, cudaArraySurfaceLoadStore));
		// 开辟 GPU 内存: cuda_Array: seed
		cudaArray *d_seed_array;
		CUDA_SAFE_CALL(cudaMalloc3DArray((cudaArray **)&d_seed_array, &channelDesc, extent3D, cudaArraySurfaceLoadStore));

		int *h_incluidos = (int *)malloc(size_int);
		int *d_incluidos;
		CUDA_SAFE_CALL(cudaMalloc((void **)&d_incluidos, size_int));
		dim3 dimBlock(16, 16, 4);
		dim3 dimGrid(32, 32, (depth + 4) / 4);

		// 将 h_track_data与 d_track_array 绑定
		cudaMemcpy3DParms track_parms = {0};
		track_parms.srcPos = make_cudaPos(0, 0, 0);
		track_parms.dstPos = make_cudaPos(0, 0, 0);
		track_parms.srcPtr = make_cudaPitchedPtr(h_track_data, width * size_uchar, width, height);
		track_parms.dstArray = d_track_array;
		track_parms.extent = make_cudaExtent(width, height, depth);
		track_parms.kind = cudaMemcpyHostToDevice;
		CUDA_SAFE_CALL(cudaMemcpy3D(&track_parms));
		// 指定表面内存
		struct cudaResourceDesc resDesc;
		memset(&resDesc, 0, sizeof(resDesc));
		resDesc.resType = cudaResourceTypeArray;
		// 创建表面内存对象 并绑定 CUDA_Array
		resDesc.res.array.array = d_track_array;
		cudaSurfaceObject_t track_surf_obj = 0;
		cudaCreateSurfaceObject(&track_surf_obj, &resDesc);

		// 将 h_seed_data与 d_tmp_array 绑定
		cudaMemcpy3DParms tmp_parms = {0};
		tmp_parms.srcPos = make_cudaPos(0, 0, 0);
		tmp_parms.dstPos = make_cudaPos(0, 0, 0);
		tmp_parms.srcPtr = make_cudaPitchedPtr(h_seed_data, width * size_uchar, width, height);
		tmp_parms.dstArray = d_tmp_array;
		tmp_parms.extent = make_cudaExtent(width, height, depth);
		tmp_parms.kind = cudaMemcpyHostToDevice;
		CUDA_SAFE_CALL(cudaMemcpy3D(&tmp_parms));
		// 指定表面内存
		struct cudaResourceDesc t_resDesc;
		memset(&t_resDesc, 0, sizeof(t_resDesc));
		t_resDesc.resType = cudaResourceTypeArray;
		// 创建表面内存对象 并绑定 CUDA_Array
		t_resDesc.res.array.array = d_tmp_array;
		cudaSurfaceObject_t tmp_surf_obj = 0;
		cudaCreateSurfaceObject(&tmp_surf_obj, &t_resDesc);

		// 将 h_seed_data与 d_seed_array 绑定
		cudaMemcpy3DParms seed_parms = {0};
		seed_parms.srcPos = make_cudaPos(0, 0, 0);
		seed_parms.dstPos = make_cudaPos(0, 0, 0);
		seed_parms.srcPtr = make_cudaPitchedPtr(h_seed_data, width * size_uchar, width, height);
		seed_parms.dstArray = d_seed_array;
		seed_parms.extent = make_cudaExtent(width, height, depth);
		seed_parms.kind = cudaMemcpyHostToDevice;
		CUDA_SAFE_CALL(cudaMemcpy3D(&seed_parms));
		// 指定表面内存
		struct cudaResourceDesc seed_resDesc;
		memset(&seed_resDesc, 0, sizeof(seed_resDesc));
		seed_resDesc.resType = cudaResourceTypeArray;
		// 创建表面内存对象 并绑定 CUDA_Array
		seed_resDesc.res.array.array = d_seed_array;
		cudaSurfaceObject_t seed_surf_obj = 0;
		cudaCreateSurfaceObject(&seed_surf_obj, &seed_resDesc);

		// DistanceTransform
		InitWithLimits<<<dimGrid, dimBlock>>>(track_surf_obj, distance_iteration_limit, lower_threshold, upper_threshold, depth, width, height);

		int iterations = 0;
		do
		{
			*h_incluidos = 0;
			CUDA_SAFE_CALL(cudaMemcpy(d_incluidos, h_incluidos, size_int, cudaMemcpyHostToDevice));
			DistanceTransform<<<dimGrid, dimBlock>>>(track_surf_obj, d_incluidos, depth, width, height, iterations);
			CUDA_SAFE_CALL(cudaDeviceSynchronize());
			CUDA_SAFE_CALL(cudaMemcpy(h_incluidos, d_incluidos, size_int, cudaMemcpyDeviceToHost));
			iterations++;
			if (iterations > distance_iteration_limit)
			{
				break;
			}
		} while (*h_incluidos != 0);

		//region_growth
		int limit = 100;
		for (int growth_bound = distance_iteration_limit; growth_bound > 0; growth_bound--)
		{
			iterations = 0;
			if (growth_bound == 1) {
				limit = 0;
			}
			do {
				*h_incluidos = 0;
				CUDA_SAFE_CALL(cudaMemcpy(d_incluidos, h_incluidos, size_int, cudaMemcpyHostToDevice));
				RegionGrowing<<<dimGrid, dimBlock>>>(tmp_surf_obj, seed_surf_obj, track_surf_obj, d_incluidos, depth, width, height, growth_bound);
				RefactorSeedData<<<dimGrid, dimBlock>>>(tmp_surf_obj, seed_surf_obj, depth, width, height);
				cudaDeviceSynchronize();
				CUDA_SAFE_CALL(cudaMemcpy(h_incluidos, d_incluidos, size_int, cudaMemcpyDeviceToHost));
				if (growth_iteration_limit != -1)
				{
					iterations++;
					if (iterations > growth_iteration_limit)
					{
						break;
					}
				}
			} while (*h_incluidos > limit);
		}

		// CUDA_SAFE_CALL(cudaMemcpy(h_seed_data, d_seed_data, size_space, cudaMemcpyDeviceToHost));

		// cudaExtent extent3d = make_cudaExtent(width, height, depth);
		cudaMemcpy3DParms myParms = {0};
		myParms.srcArray = d_seed_array;
		myParms.srcPos = make_cudaPos(0, 0, 0);
		myParms.dstPos = make_cudaPos(0, 0, 0);
		myParms.dstPtr = make_cudaPitchedPtr(h_seed_data, width * size_uchar, width, height);
		myParms.extent = make_cudaExtent(width, height, depth);
		myParms.kind = cudaMemcpyDeviceToHost;
		CUDA_SAFE_CALL(cudaMemcpy3D(&myParms));

		free(h_incluidos);
		// cudaFree(d_seed_data);
		// 解除绑定并释放内存
		cudaFreeArray(d_track_array);
		// cudaFree(d_track_data);
		cudaDestroySurfaceObject(track_surf_obj);
		cudaDestroySurfaceObject(tmp_surf_obj);
		cudaDestroySurfaceObject(seed_surf_obj);
		cudaFree(d_incluidos);
		// cudaFree(d_tmp_data);
		cudaFreeArray(d_tmp_array);
		cudaFreeArray(d_seed_array);
	}
}
