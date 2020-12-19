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

#define dimnum 2

typedef struct dataPoint
{
    float x;
    float y;
    int clusterNumber;
    float radius;
} point;

vector<point> get_data(string filepath)
{

    ifstream file(filepath.c_str());
    string str;
    string delimiter = ",";
    vector<point> p;
    point tmp;

    while (getline(file, str))
    {
        size_t pos = 0;
        string x;
        while ((pos = str.find(delimiter)) != string::npos)
        {
            x = str.substr(0, pos);
            tmp.x = stof(x);
            // cout << x << '\t';
            str.erase(0, pos + delimiter.length());

            tmp.y = stof(str);
            p.push_back(tmp);
        }
    }
    return p;
}

void printPoint(dataPoint p)
{
    cout << p.x << '\t' << p.y << '\t' << p.clusterNumber << endl;
}

void printVector(vector<point> &point)
{
    for (int i = 0; i < point.size(); i++)
    {
        printPoint(point[i]);
    }
    cout << endl;
}

void graph_state2file(ofstream &outfile, vector<point> &point)
{
    outfile.setf(ios::fixed);
    for (int i = 0; i < point.size(); i++)
    {
        outfile << setprecision(2) << point[i].x << ',' << point[i].y << ',' << point[i].clusterNumber << endl;
    }
}

double getDist_xy(dataPoint a, dataPoint b)
{
    double dist = 0;
    dist = sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2));
    return dist;
}

void getCluRadius(vector<point> &data, int k, point *Centroid, float *cluRadius)
{
}

bool isCentrMoving(point p1, point p2)
{
    if (p1.x != p2.x || p1.y != p2.y)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void init_cluster_centers(vector<point> &data, int k, point *Centroid)
{
    srand((unsigned)time(0));
    int randomNumber;
    int randomSize = data.size();
    int i;
    vector<int> diff;
    for (i = 0; i < k; i++)
    {
        randomNumber = (rand() % (randomSize)) + 0; //random num in [0,10)
        while (count(diff.begin(), diff.end(), randomNumber))
        {
            randomNumber = (rand() % (randomSize)) + 0; //random num in [0,10)
        }
        diff.push_back(randomNumber);
        data[randomNumber].clusterNumber = (i + 1);
        Centroid[i] = data[randomNumber];
    }
}

void update_clusters(vector<point> &data, int k, point *Centroid)
{
    int i, j, distance;
    float bestMiniDist;
    float *maxRadius = new float[k];
    int pointStillMoving = 0;
    for (i = 0; i < k; i++)
    {
        maxRadius[i] = 0;
    }
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
            if (distance > maxRadius[j])
            {
                maxRadius[j] = distance;
                Centroid[j].radius = maxRadius[j];
            }
        }
    }
    delete maxRadius;
}

int recalculate_centroids(vector<point> &data, int k, point *Centroid)
{
    int i, j, cluster, index, isStillMoving = 0;
    float *count = new float[k];
    float *sumX = new float[k];
    float *sumY = new float[k];
    dataPoint *preCentroid = new dataPoint[k];

    for (j = 0; j < k; j++)
    {
        preCentroid[j].x = Centroid[j].x;
        preCentroid[j].y = Centroid[j].y;
        preCentroid[j].clusterNumber = Centroid[j].clusterNumber;
    }

    for (i = 0; i < data.size(); i++)
    {
        cluster = data[i].clusterNumber;
        index = data[i].clusterNumber - 1;
        sumX[index] += data[i].x;
        sumY[index] += data[i].y;
        count[index]++;
    }

    for (i = 0; i < k; i++)
    {
        Centroid[i].x = sumX[i] / count[i];
        Centroid[i].y = sumY[i] / count[i];
    }

    for (j = 0; j < k; j++)
    {
        if (isCentrMoving(preCentroid[j], Centroid[j]))
        {
            isStillMoving = 1;
        }
    }

    delete count;
    delete sumX;
    delete sumY;
    delete preCentroid;

    return isStillMoving;
}

void kMean(vector<point> &data, int k)
{
    ofstream pointState("procedure.txt");
    ofstream onefile("onestep.txt");
    ofstream outcentr("centroid.txt");

    int isStillMoving = 1, step = 0;
    dataPoint *Centroid = new dataPoint[k];
    float *cluRadius = new float[k];

    init_cluster_centers(data, k, Centroid);

    while (isStillMoving)
    {
        step++;

        update_clusters(data, k, Centroid);
        isStillMoving = recalculate_centroids(data, k, Centroid);

        graph_state2file(pointState, data);

        for (int i = 0; i < k; i++)
        {
            outcentr.setf(ios::fixed);
            outcentr << setprecision(2) << Centroid[i].x << ',' << Centroid[i].y << ',' << Centroid[i].clusterNumber << ',' << Centroid[i].radius << endl;
        }
    }

    graph_state2file(onefile, data);

    cout << "step:" << step << endl;
    delete Centroid;
}

int main()
{
    string fileName = "datakmean.txt";
    vector<point> data = get_data(fileName);

    int k = 2;

    kMean(data, k);
    cout << "Cluster result:\n";
    printVector(data);

    return 0;
}