# -*- coding: utf-8 -*- 
import sys
sys.setrecursionlimit(100) # 10000 is an example, try with different values

def avgs(args=[]):
	'''
		Tính trung bình cộng của dãy tham số
	'''
	sum = 0.00
	num = 0.00
	for i in args:
		num = num + 1
		sum = sum + float(i)
	if num != 0:
		average = sum/num
		average	=	round(average, 1)
		return average
	else:
		return 0

def append_to_list( list_, *values):
	'''Adds `values` to the end of `list`.
	Example:
	| Append To List | ${L1} | xxx |   |   |
	| Append To List | ${L2} | x   | y | z |
	=>
	- ${L1} = ['a', 'xxx']
	- ${L2} = ['a', 'b', 'x', 'y', 'z']
	'''
	for value in values:
		list_.append(value)
			
def combine_lists(*lists):
	'''Combines the given `lists` together and returns the result.

	The given lists are not altered by this keyword.

	Example:
	| ${x} = | Combine List | ${L1} | ${L2} |       |
	| ${y} = | Combine List | ${L1} | ${L2} | ${L1} |
	=>
	- ${x} = ['a', 'a', 'b']
	- ${y} = ['a', 'a', 'b', 'a']
	- ${L1} and ${L2} are not changed.
	'''
	ret = []
	for item in lists:
		ret.extend(item)
	return ret

def	add(arg1, arg2):
	num1 = int(arg1)
	num2 = int(arg2)
	return	(num1+num2)

def all_bg_minAvg(minAvg, _diem=[]):
	'''Kiểm tra các giá trị điểm trong mảng _diem có đều lớn hơn minAvg hay không'''
	for mark in _diem:
		if float(mark) < float(minAvg):
			return 0
	return 1
	
def tinh_hoc_luc(diemTheDuc, _avg, diem=[] ):
	'''
		Xét học lực của học sinh dựa trên điểm tổng kết các môn học, điểm xếp loại môn Thể dục
		1. Loại Giỏi:
			- Điểm trung bình các môn học từ 8,0 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 8.0 trở lên; 
			- Không có môn học nào điểm trung bình dưới 6,5;
			- Các môn học đánh giá bằng nhận xét đạt loại Đ.
		2. Loại khá, nếu có đủ các tiêu chuẩn sau đây:
			- Điểm trung bình các môn học từ 6,5 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 6,5 trở lên; 
			- Không có môn học nào điểm trung bình dưới 5,0;
			- Các môn học đánh giá bằng nhận xét đạt loại Đ.
		3. Loại trung bình, nếu có đủ các tiêu chuẩn sau đây:
			- Điểm trung bình các môn học từ 5,0 trở lên, trong đó điểm trung bình của 1 trong 2 môn Toán, Ngữ văn từ 5,0 trở lên; 
			- Không có môn học nào điểm trung bình dưới 3,5;
			- Các môn học đánh giá bằng nhận xét đạt loại Đ.
		4. Loại yếu: Điểm trung bình các môn học từ 3,5 trở lên, không có môn học nào điểm trung bình dưới 2,0.
		5. Loại kém: Các trường hợp còn lại.
	'''
	avgToan = float(diem[0])
	avgVan = float(diem[5])
	avg = float(_avg)
	if (avg >= 8.0):		
		if (diemTheDuc == unicode("Đ", 'utf-8') and all_bg_minAvg(6.5, diem) == 1):
			if avgToan >= 8.0 or avgVan >= 8.0:
				return unicode("Giỏi", 'utf-8')
	if (avg >= 6.5):
		if (diemTheDuc == unicode("Đ", 'utf-8') and all_bg_minAvg(5.0, diem) == 1):
			if avgToan >= 6.5 or avgVan >= 6.5:
				return unicode("Khá", 'utf-8')
	if (avg >= 5.0):
		if (diemTheDuc == unicode("Đ", 'utf-8') and all_bg_minAvg(3.5, diem) == 1):
			if avgToan >= 5.0 or avgVan >= 5.0:
				return unicode("TB", 'utf-8')
	if (avg >= 3.5):
		if (all_bg_minAvg(2.0, diem) == 1):
				return unicode("Yếu", 'utf-8')		
	return unicode("Kém", 'utf-8')		
	
def tinh_danh_hieu(hocluc, hanhkiem):
	'''
		Xét danh hiệu của học sinh dựa trên Học lực và Hạnh kiểm
		1. Học sinh giỏi:
			- Học lực giỏi, Hạnh kiểm tốt
		2. Học sinh Tiên tiến
			- Học lực Khá, Hạnh kiểm khá trở lên hoặc Học lực Giỏi, Hạnh kiểm khá
	'''
	if (hocluc == unicode("Giỏi",'utf-8')):
		if (hanhkiem == "T"):
			return "HSG"
		elif (hanhkiem == "K"):
			return "HSTT"
	elif (hocluc == unicode("Khá",'utf-8')):
		if (hanhkiem == "T" or hanhkiem == "K"):
			return "HSTT"
	return ""

