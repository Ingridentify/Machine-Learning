<p align="center">
    <img src="https://github.com/Ingridentify/Ingridentify/blob/dev/app/src/main/res/drawable/typography_color.png?raw=true"  width="400">
</p>

# Machine Learning

## Team

| Name                          | Student ID  | Path                 |
| ----------------------------- | ----------- | -------------------- |
| Ryan Reynickha Fatullah       | M296BSY1298 | Machine Learning     |
| Syifa Nur'Afni Hidayat        | M494BSX0800 | Machine Learning     |

## About The Project 
In order to create our model, we utilized Machine Learning with the architecture of CNN (Convolutional Neural Network). The dataset we used for training the model is called [Fruit and Vegetables SSM](https://www.kaggle.com/datasets/shadikfaysal/fruit-and-vegetables-ssm).

## Endpoint API
we have a endpoint that can be used to classify fruits & vegetables images with architecture of CNN (Convolutional Neural Network).
<table width="100%">
    <tr>
        <th>Method</th>
        <th>Routes</th>
        <th>Type</th>
        <th>Description</th>
    </tr>
    <tr>
        <td colspan="4"><b>Predict</b></td>
    </tr>
     <tr>
        <td>POST</td>
        <td>/predict</td>
        <td>multipart/form-data</td>
        <td>Predict uploaded fruits & vegetables images</td>
    </tr>
</table>

## Built With
- Uvicorn (fastapi)
- Tensorflow
- Pillow
- Python-multipart
- Numpy


# Try This Project
Dive into this project and discover its functionalities.

### Prerequisites
Before you start, ensure that you have the following software installed on your system:
- Python 3.10.x
- Pip 22.x.x
- Git LFS

### Installation
1. Clone the repo
   
   ```sh
    git clone https://github.com/Ingridentify/Machine-Learning.git
    git lfs pull
   ```
2. Move to `./Machine-Learning` directory

   ```sh
    cd ./Machine-Learning
   ```
   
3. Install requirements using PIP

   ```sh
    pip install -r requirements.txt
   ```

5. Run ml service application

   ```sh
    python app.py 
   ```

### Requirements
- fastapi
- tensorflow
- Pillow
- numpy
- uvicorn[standard]
- python-multipart

### Important Link
- [Capstone Notebook](https://colab.research.google.com/drive/10-Vj-qnpRBRkzFeAxomX0ih3-WGJAkH_?usp=sharing )
- [Dataset](https://www.kaggle.com/datasets/shadikfaysal/fruit-and-vegetables-ssm)
