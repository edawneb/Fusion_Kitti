

#include <iostream>
#include <thread>
#include <ctime>
#include <ctype.h>
#include <cuda_runtime.h>
//#include <libcpuid.h>
#include <vector>

using namespace std;

int main(){

    size_t free;
    size_t total;
    cudaMemGetInfo(&free, &total);

    cudaDeviceProp currentDevice;
    int present = thread::hardware_concurrency();

    cout<<"Available Memory: "<<free<<" bytes, Total Memory: "<<total<<" bytes"<< endl;
    cout<<"Threads Available: "<<present<<endl;


    return 0;
}

//class basically works by creating a series of records of the system status stored in the dataAggregator sub-class.
//each instance of cudaDeviceProps holds the instanteous read outs of each cuda device stored in an array of cudaDeviceProps.
//Along specific intervals, the idea is to instantiate a dataAggregator at each timestamp, and append it to the vector of dataAggregators
//in SystemInfoAggregator. once the program runs, the SystemInfoAggregator vector will contain a continous record of device utilization.
class SystemInfoAggregator
{
    private:
        static size_t class_free;
        static size_t class_total;
        static int class_deviceCount;
        static int class_cpuCount;
        static int class_gpuCount;
        static time_t startTime;
        time_t now;
        

        class dataAggregator
        {   public:
                time_t timestamp;
                size_t free;
                size_t total;
                int deviceCount;
                int cpuCount;
                int gpuCount;
                cudaDeviceProp *deviceCache;
                dataAggregator(){
                    timestamp = NULL;
                    free = NULL;
                    total = NULL;
                    deviceCount = NULL;
                    cpuCount = NULL;
                    gpuCount = NULL;
                    deviceCache = NULL;
                };
                dataAggregator(size_t class_total, int class_deviceCount, int class_cpuCount, int class_gpuCount){
                    timestamp = NULL;
                    free = class_total;
                    total = NULL;
                    deviceCount = class_deviceCount;
                    cpuCount = class_cpuCount;
                    gpuCount = class_gpuCount;
                    deviceCache = NULL;
                };

                

        };
        
        dataAggregator working_var;
        vector<dataAggregator> dataPile;

        

        dataAggregator getCurrentInfo()
        {
            dataAggregator localCopy(class_total, class_deviceCount, class_cpuCount, class_gpuCount);
            time(&now);
            localCopy.timestamp = difftime(startTime, now);
            cudaMemGetInfo(&localCopy.free, &localCopy.total);
            getDeviceData(localCopy);
            return localCopy;
        }
        


        void getDeviceData(dataAggregator localCopy)
        {
            if (localCopy.gpuCount!=NULL){
                for(int i=0; i<localCopy.gpuCount; i++)
                {
                    cudaGetDeviceProperties(&localCopy.deviceCache[i], i);
                }
            }

        }


    public:
        SystemInfoAggregator()
        {
            time(&startTime);
            cudaGetDeviceCount(&class_gpuCount); //load original number of devices
            cudaMemGetInfo(&class_free, &class_total); //Using this to just get the total mem available and an initial snapshot
            class_cpuCount = thread::hardware_concurrency(); //Getting threadCount
            class_deviceCount = class_gpuCount+class_cpuCount;
            
            working_var = getCurrentInfo();
            working_var.deviceCache = new cudaDeviceProp[class_gpuCount];
            
        }   
        ~SystemInfoAggregator()
        {
            
        }
        void newDataPoint()
            {
                dataPile.push_back(getCurrentInfo());
            }    

        
};