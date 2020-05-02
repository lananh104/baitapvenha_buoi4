""" Bài tập:
Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
"""
# Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
while True:
    a=list(input("Mời nhập list: " ))
    if len(a)<5:
        print("List vừa nhập có ít hơn 5 phần tử. Mời nhập lại!")
    else:
        b=a[None:5]
        print("List mới là: ",b)
        break
# Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
a=[1,2,3,4,5,6,7,8]
s=0
t=1
for i in a:
    s+=i
    t*=i
print("Tổng các phần tử là: ",s)
print("Tích các phần tử là: ",t)
#Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
a=[2,4,6,1,3,4,55,7,4]
a.sort(reverse=True)
print("Số lớn nhất trong list là: ",a[0])
print("Số nhỏ nhất trong dãy là: ",a[len(a)-1])
#Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
a=list(input("Mời nhập list: "))
s=input("Mời nhập chuỗi: ")
n=int(input("Mời nhập vị trí cần ghép thêm chuỗi s: "))
a.insert(n,s)
print(a)
#Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím
a=list(input("Mời nhập chuỗi: "))
n=int(input("Mời nhập độ dài phần đầu của list: "))
b=a[None:n]
c=a[n:None]
print("Phần đầu của list là: ", b)
print("Phần còn lại của list là: ",c)
#Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
#        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
a=input("Mời nhập list: ")
max=a.count(a[0])
for i in a:
    if a.count(i)>max:
        max=i
    else:
        max=a[0]
print("Phần tử xuất hiện nhiều nhất trong dãy là: ", max)
# Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
a=["abca","cdbd","dhg"]
d=0
print(a)
for x in a:
    if len(x)>=2 and x[0]==x[-1]:
        d+=1
print("Số các chuỗi thảo mãn là: ",d)
#Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
a=list(input("Mời nhập list a: "))
b=list(input("Mời nhập list b: "))
test=0
for x in a:
    for y in b:
        if x==y:
            test=1
if test==1:
    print("2 list có phần tử chung")
else:
    print("2 list không có phần tử chung")
#Bài 08: Cho list các số nguyên dương A.
#       Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
A=[1,2,3,4,5]
d=0
for i in range(len(A)):
    for j in range(len(A)):
        if i<j and A[i]>A[j]:
            d+=1
print(d)
Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
import numpy as np
A=np.array([[1,2,3],[2,3,4],[3,3,4]])
B=np.array([[1,1,3],[1,4,3],[2,2,1]])
C=np.dot(A,B)
print("Kết qủa của phép nhân 2 ma trận A và B là:\n ",C)
'''Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
'''

a=[1,2,3,4,5,6,6,7,1,2,7,7]
b=set(a)
print(b)
print(len(b))
