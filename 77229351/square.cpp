#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstdlib>
#include <iostream>

static int WIDTH = 640;
static int HEIGHT = 480;
int renders = 0;
double PI = 3.1415;
double trans = 0;
double x {0};
float rotatex = 0, rotatey = 0, mousex = 0, mousey = 0;
bool dragging = false;
int keyArr[350];

static void Initialize(void) {
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glClearColor(0.0, 0.0, 0.0, 1.0);
}

static void Update(GLFWwindow* window) {
    if (keyArr[GLFW_KEY_ESCAPE])
        glfwSetWindowShouldClose(window, 1);
    rotatex += keyArr[GLFW_KEY_LEFT] - keyArr[GLFW_KEY_RIGHT];
    rotatey += keyArr[GLFW_KEY_UP] - keyArr[GLFW_KEY_DOWN];
}

static void RenderScene(GLFWwindow* window) {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.5, 0.5, 0.5);
        if(renders == 0){
        glScalef(1.0f, 2.0f, 1.0f);
    }
    renders++;
    if(x > -1){
        x -= 0.01;
    }else{
        x = 1;
    }


    glBegin(GL_LINE_LOOP);
    glVertex2f(x -0.25 , 0);
    glVertex2f(x, 0.25);
    glVertex2f(x +0.25, 0);
    glEnd();
    glFlush();
}

static void KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    keyArr[key] = action;
}


int main(int argc, char** argv) {
    GLFWwindow* window;

    glfwInit();
    window = glfwCreateWindow(WIDTH, HEIGHT, argv[0], NULL, NULL);
    glfwMakeContextCurrent(window);
    glfwWindowHint(GLFW_SAMPLES, 4);
    Initialize();
    glfwSetKeyCallback(window, KeyCallback);
    while (!glfwWindowShouldClose(window)) {
        Update(window);
        RenderScene(window);
        glfwSetTime(0);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwDestroyWindow(window);
    return 0;
}
