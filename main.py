# Gradient Descent algorithm

data_set_x = []
data_set_y = []
data_set_tc = []

data_size = int(input("Enter data size: "))

w0 = 0
w1 = 0
j = 0
k = 0
iteration = 1000

for i in range(0, int(data_size)):
    x = int(input("Enter x: "))
    y = int(input("Enter y(original output): "))
    data_set_x.append(x)
    data_set_y.append(y)

for j in range(iteration):
    cost = 0
    total_cost = 0
    r_cost = 0
    temp = total_cost
    for i in range(0, int(data_size)):
        predicted_output = w0 + (w1 * data_set_x[i])
        r_cost += (predicted_output - data_set_y[i])
        cost += (data_set_y[i] - predicted_output) ** 2
        data_set_tc.append(total_cost)
    total_cost = (1 / (2 * data_size)) * cost
    # print(f"r_cost = {r_cost}")
    w0 = w0 - (0.01 * (1 / data_size)) * r_cost
    w1 = w1 - (0.01 * (1 / data_size) * r_cost) * data_set_x[j % 5]
    # print(f"w0 = {w0}")
    # print(f"w1 = {w1}")
    # print(f"total_cost = {total_cost}")
    if abs(total_cost - temp) <= 0.004:
        # print(temp)
        # print(total_cost)
        break

# print(f"w0 = {w0}")
# print(f"w1 = {w1}")
print(f"Gradient Descent algorithm for linear regression equation is: {w0} + {w1}x")



















# # Linear Regression
# # For numerical analysis we know,
# # m = (x_mean * y_mean - xy_mean) / ((x_mean)^2 - (x_mean^2)_mean)
# # c = (y-mean) - m * (x-mean)
# data_set_x = []
# data_set_y = []
#
# x_sum = 0
# y_sum = 0
# xy_sum = 0
# x_square_sum = 0
#
# data_size = int(input("Enter data size: "))
#
# for i in range(0, int(data_size)):
#     x = int(input("Enter pizza size(inch): "))
#     y = int(input("Enter pizza price: "))
#     data_set_x.append(x)
#     data_set_y.append(y)
#     # For equation value
#     x_sum += x
#     y_sum += y
#     xy_sum += x * y
#     x_square_sum += x ** 2
#
# x_mean = x_sum / data_size
# y_mean = y_sum / data_size
# xy_mean = xy_sum / data_size
# x_mean_square = x_mean ** 2
# x_square_mean = x_square_sum / data_size
#
# try:
#     m = ((x_mean * y_mean) - xy_mean) / (x_mean_square - x_square_mean)
# except ZeroDivisionError:
#     m = 0
#
# c = y_mean - (m * x_mean)
#
# m_final = "{:.2f}".format(m)
# c_final = "{:.2f}".format(c)
#
# if c >= 0:
#     print(f"\nSo, the line equation for linear regression is: {m_final}x+{c_final}")
# else:
#     print(f"\nSo, the line equation for linear regression is: {m_final}x{c_final}")
#
# predicted_mean = 0
# original_mean = 0
#
# for i in range(0, int(data_size)):
#     predicted_mean += (m * data_set_x[i] + c - y_mean) ** 2
#     original_mean += (data_set_y[i] - y_mean) ** 2
#
# try:
#     accuracy = (predicted_mean / original_mean) * 100
# except ZeroDivisionError:
#     accuracy = 0
#
# print(f"\nSo R-Squared Value or Accuracy of our model is: {accuracy}%")
#
# print("Guess a pizza price from pizza size(inch): Y/N")
# s = input()
# if s == "Y":
#     guessed_num = int(input("Enter the size of pizza(inch): "))
#     res = m * x + c
#     print(f"Price of the pizza will be: {res}")