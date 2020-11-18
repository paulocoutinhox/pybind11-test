#include <fstream>
#include <iostream>
#include <string>
#include <thread>

#include "pybind11/embed.h"

namespace py = pybind11;

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

        PyErr_SetInterrupt();

        std::cout << "+ Interrupted" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cout << "@ " << e.what() << std::endl;
    }
}

int main()
{
    std::cout << "+ Starting..." << std::endl;

    std::thread th(python_executor, "example.py");
    auto threadId = th.get_id();
    std::cout << "+ Thread: " << threadId << std::endl;

    //th.detach();
    th.join();

    std::cout << "+ Finished" << std::endl;

    return EXIT_SUCCESS;
}