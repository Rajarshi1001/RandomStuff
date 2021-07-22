#include<opencv2/opencv.hpp>
#include<iostream>
using namespace std;
using namespace cv;

int main(){

    string img_name = "helc.jpg";
    Mat image; Mat dst; Mat gray; Mat br;
    image = imread(img_name);
    resize(image, dst, Size(), 0.5, 0.5);
    cvtColor(dst, gray, cv::COLOR_BGR2GRAY);
    GaussianBlur(gray, br,cv::Size(101,101), 3,3, 4);
    //medianBlur(gray,br,7);
    //TODOadaptiveThreshold(gray, br, 0,255, );
    imshow("output", br);

    waitKey(0);
    destroyAllWindows();
}