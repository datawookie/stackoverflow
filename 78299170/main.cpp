#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <iostream>

int main(int argc, char** argv)
{
    std::cout << "Initialize GLFW." << std::endl;
    if (!glfwInit())
    {
        std::cout << "Cannot initialize GLFW." << std::endl;
        return -1;
    }
    std::cout << "Done!" << std::endl;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);
    // glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    std::cout << "Create a window." << std::endl;
    GLFWwindow* window = glfwCreateWindow(1024, 768, "Hello World", NULL, NULL);

    if (!window)
    {
        glfwTerminate();
        std::cout << "Window creating failed." << std::endl;
        return -1;
    }
    std::cout << "Done!" << std::endl;

    std::cout << "Make context current." << std::endl;
    glfwMakeContextCurrent(window);

    const char* errorDesc;
    if (glfwGetError(&errorDesc) != GLFW_NO_ERROR)
    {
        std::cout << "Making context current failed:\n" << errorDesc << std::endl;
        return -1;
    }
    std::cout << "Done!" << std::endl;

    // TEST
    glfwMakeContextCurrent(window);
glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
glClear(GL_COLOR_BUFFER_BIT);
GLenum error = glGetError();

    std::cout << "Initialise GLEW." << std::endl;
    glewExperimental = GL_TRUE;
    GLenum err = glewInit();
    if (GLEW_OK != err)
    {
        std::cout << glewGetErrorString(err) << std::endl;
        return -1;
    }
    std::cout << "Done!" << std::endl;

    std::cout << "Clear errors." << std::endl;
    glGetError();
    std::cout << "Done!" << std::endl;

const GLubyte* oglVersion = glGetString(GL_VERSION);
if (oglVersion != nullptr) {
    std::cout << "OpenGL version: " << oglVersion << std::endl;
} else {
    std::cout << "Failed to retrieve OpenGL version." << std::endl;
}

    // auto ver = glGetString(GL_VERSION);

    // if (!ver)
    // {
    //     std::cout << "OpenGl error. Something went wrong." << std::endl;
    //     // glGetError(); // This line produces crash
    //     return -1;
    // }

    // std::cout << "OpenGL version: " << ver << std::endl;

    glfwTerminate();
    return 0;
}
