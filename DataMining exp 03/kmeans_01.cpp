#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include <iomanip>
#include <fstream>
#include <algorithm>
using namespace std;

typedef struct dataPoint
{
    float score[10];
    int clusterNumber;
    float radius;
} point;

bool get_data(string filepath, vector<point> &p)
{

    ifstream file(filepath.c_str());
    if (file.is_open())
    {
        string str;
        string delimiter = ",";
        point tmp;

        while (getline(file, str))
        {
            int index_In_Struct_score = 0;
            size_t pos = 0;
            string token;
            tmp.clusterNumber = 0;

            while ((pos = str.find(delimiter)) != string::npos)
            {

                token = str.substr(0, pos);
                tmp.score[index_In_Struct_score] = stof(token);
                index_In_Struct_score++;
                // std::cout << token << std::endl;
                str.erase(0, pos + delimiter.length());
            } //end split string
            tmp.score[index_In_Struct_score] = stof(str);
            p.push_back(tmp);
        } //end read txt

        return true;
    }
    else
    {
        return false;
    }
}

void graph_state2file(ofstream &outfile, vector<point> &point)
{
    outfile.setf(ios::fixed);
    for (int i = 0; i < point.size(); i++)
    {
        for (int j = 0; j < 10; j++)
        {
            outfile << setprecision(6) << point[i].score[j];
            outfile << ',';
        }
        outfile << point[i].clusterNumber << endl;
    }
}

void printPoint(dataPoint p)
{
    cout.setf(std::ios::right);
    cout.width(9);
    for (int i = 0; i < 10; i++)
    {
        cout.width(9);
        cout << setiosflags(ios::fixed) << setprecision(6) << p.score[i];
        if (i != 9)
        {
            cout << ',';
        }
    }
    cout.width(7);
    cout << "   " << p.clusterNumber;
}

void printVector(vector<point> &point)
{
    for (int i = 0; i < point.size(); i++)
    {
        printPoint(point[i]);
        cout << endl;
    }
    cout << endl;
}

bool isCentrMoving(point p1, point p2)
{
    for (int i = 0; i < 10; i++)
    {
        if (p1.score[i] != p2.score[i])
        {
            return true;
        }
    }
    return false;
}

void init_cluster_centers(vector<point> &data, int k, point *Centroid)
{
    srand((unsigned)time(0));
    int randomNumber;
    int randomSize = data.size();
    int i, j;
    vector<int> diff;
    for (i = 0; i < k; i++)
    {
        randomNumber = (rand() % (randomSize)) + 0; //random num in [0,10)
        // 确保选取不同的初始质心
        while (count(diff.begin(), diff.end(), randomNumber))
        {
            randomNumber = (rand() % (randomSize)) + 0; //random num in [0,10)
        }
        diff.push_back(randomNumber);
        data[randomNumber].clusterNumber = (i + 1);
        for (j = 0; j < 10; j++)
        {
            Centroid[i].score[j] = data[randomNumber].score[j];
        }
        Centroid[i].clusterNumber = (i + 1);
        // Centroid[i].clusterNumber = data[randomNumber].clusterNumber;
    }
}

float getDist_xy(dataPoint a, dataPoint b)
{
    float dist = 0;
    float powResult = 0;
    for (int i = 0; i < 10; i++)
    {
        powResult += pow(a.score[i] - b.score[i], 2);
    }
    dist = sqrt(powResult);
    return dist;
}

void update_clusters(vector<point> &data, int k, point *Centroid)
{
    int i, j;
    float distance;
    float bestMiniDist;
    int stillMoving = 0;
    int pointStillMoving = 0;
    for (i = 0; i < data.size(); i++)
    {
        bestMiniDist = 32767;

        for (j = 0; j < k; j++)
        {
            distance = getDist_xy(data[i], Centroid[j]);
            if (distance < bestMiniDist)
            {
                bestMiniDist = distance;
                data[i].clusterNumber = Centroid[j].clusterNumber;
            }
        }
    }
}

int recalculate_centroids(vector<point> &data, int k, point *Centroid)
{
    int i, j, index, isStillMoving = 0;

    float **sumEachSocre;
    sumEachSocre = new float *[10]; //10门成绩
    for (i = 0; i < 10; i++)
    {
        sumEachSocre[i] = new float[k];
    }
    for (i = 0; i < 10; i++)
    {
        for (j = 0; j < k; j++)
        {
            sumEachSocre[i][j] = 0;
        }
    }
    float *count = new float[k];
    for (i = 0; i < k; i++)
    {
        count[i] = 0;
    }
    dataPoint *preCentroid = new dataPoint[k];

    for (j = 0; j < k; j++)
    {
        for (i = 0; i < 10; i++)
        {
            preCentroid[j].score[i] = Centroid[j].score[i];
        }
        preCentroid[j].clusterNumber = Centroid[j].clusterNumber;
    }
    for (i = 0; i < data.size(); i++)
    {
        index = data[i].clusterNumber - 1;
        for (j = 0; j < 10; j++)
        {
            sumEachSocre[j][index] += data[i].score[j];
        }
        count[index]++;
    }
    for (i = 0; i < k; i++)
    {
        for (j = 0; j < 10; j++)
        {
            Centroid[i].score[j] = sumEachSocre[j][i] / count[i];
        }
    }
    for (i = 0; i < k; i++)
    {
        if (isCentrMoving(preCentroid[i], Centroid[i]))
        {
            isStillMoving = 1;
        }
    }
    delete[] preCentroid;
    for (i = 0; i < 10; i++)
    {
        delete[] sumEachSocre[i];
    }
    delete[] count;
    delete[] sumEachSocre;
    return isStillMoving;
}

void kMean(vector<point> &data, int k)
{
    int isStillMoving = 1, step = 0;
    dataPoint *Centroid = new dataPoint[k];

    init_cluster_centers(data, k, Centroid);
    while (isStillMoving)
    {
        update_clusters(data, k, Centroid);
        isStillMoving = recalculate_centroids(data, k, Centroid);
        if (isStillMoving == 1)
        {
            step++;
        }
    }
    cout << "Total step: " << step << endl;
    delete Centroid;
}
int main()
{
    string fileName = "./sourceData/stuScore_After_z-score.txt";
    ofstream outResult("./output/clustering_result_Stu.txt");

    vector<point> scoreData;
    int k = 2;
    dataPoint *Centroid = new dataPoint[k];

    if (get_data(fileName, scoreData))
    {
        // printVector(scoreData);
        // init_cluster_centers(scoreData, k, Centroid);
        // printVector(scoreData);
        kMean(scoreData, k);
    }
    else
    {
        cout << "No such file: " << fileName << endl;
    }

    printVector(scoreData);
    // for (int j = 0; j < 2; j++)
    // {
    //     printPoint(Centroid[j]);
    //     cout << endl;
    // }
    // for (int j = 0; j < 2; j++)
    // {
    //     printPoint(Centroid[j]);
    //     cout << endl;
    // }
    graph_state2file(outResult, scoreData);

    // printPoint(scoreData[0]);
    // cout << endl;
    // printPoint(scoreData[1]);
    // cout << endl;
    // cout << getDist_xy(scoreData[0], scoreData[1]) << endl;
}