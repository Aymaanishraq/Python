import cv2, numpy as np,matplotlib.pyplot as plt

def display(title,img,cmap=None):
    plt.figure(figsize=(6,6))
    plt.imshow(img if cmap is None else cv2.cvtColor(img,cmap))
    plt.title(title);plt.axis("off");plt.show()
def edge_activity(path):
    img=cv2.imread(path)
    if img is None: return print("Image not found")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    display("Original",img,cv2.COLOR_BGR2RGB)
    display("Grayscale",gray)
    def sobel():
        sx,sy=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3), cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
        return cv2.bitwise_or(sx.astype(np.uint8),sy.astype(np.uint8))
    def canny():
        l,u=map(int,[input("Lower (default 100):") or 100,input("Upper (default 200):") or 200])
        return cv2.Canny(gray,1,u)
    def laplaciam():return cv2.Laplacian(gray,cv2.CV_64F).astype(np.uint8)
    
    def blur(): return cv2.GaussianBlur(img,(int(input("Kernel (odd, default 5):") or 5),)*2,0)

    def median(): return cv2.medianBlur(img,int(input("Kernel (odd, default 5):") or 5))
    actions = {
        "1":("Sobel Edge",sobel),
        "2":("Canny Edge",canny),
        "3":("Laplaciam",laplaciam),
        "4":("Gaussian Blur",blur),
        "5":("Median Filter",median)
    }
    while True:
        print("\n1.Sobel 2.Canny 3.Laplaciam  4.Blur 5.Median 6.Exit")
        choice = input("Choose(1-6)")
        if choice=="6":break
        if choice in actions:
            title,func = actions[choice]
            display(title,func())
        else:
            print("Invalid choice")
edge_activity("imag.jpg")
