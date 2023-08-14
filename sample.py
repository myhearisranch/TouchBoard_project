import time

# 初期化
total_distance = 0
lap_count = 0
total_time = 0

# 泳ぐ距離を入力する
print("泳ぐ距離を入力してください")
race_distance = int (input())

start_signal = input('Push "ENTER" to Start')
start_time = time.time()

#ラップタイム
while  race_distance > total_distance: 
  stop_signal = input('Push "ENTER" to Stop')
  stop_time = time.time()
  result = stop_time - start_time
  total_distance += 50
  total_time += result
  start_time = stop_time
  print(f"{total_distance}mのタイム:{result:.3f} sec")

#合計タイムを表示
print(f"合計タイム{total_time:.3f} sec")
