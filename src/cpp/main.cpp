#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <atomic>
#include <chrono>

#include "pybind11/embed.h"

namespace py = pybind11;

std::atomic<bool> stopped(false);
std::atomic<bool> executed(false);

void python_executor(const std::string &file_path)
{
    try
    {
        std::cout << "+ Executing python script..." << std::endl;

        std::ifstream ifs(file_path);
        std::string content((std::istreambuf_iterator<char>(ifs)), (std::istreambuf_iterator<char>()));

        py::scoped_interpreter guard{};

        py::exec(content);

        std::cout << "+ Finished python script" << std::endl;

        if (stopped)
        {
            PyErr_SetInterrupt();
            std::cout << "+ Terminated by user" << std::endl;
            executed = true;
            return;
        }
    }
    catch (const std::exception &e)
    {
        std::cout << "@ " << e.what() << std::endl;
    }

    executed = true;

    std::cout << "+ Terminated normal" << std::endl;
}

int main()
{
    std::cout << "+ Starting..." << std::endl;

    std::thread th(python_executor, "example.py");
    auto threadId = th.get_id();
    std::cout << "+ Thread: " << threadId << std::endl;

    th.detach();

    stopped = true;

    while (!executed)
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        std::cout << "+ Waiting..." << std::endl;
    }

    std::cout << "+ Finished" << std::endl;

    return EXIT_SUCCESS;
}