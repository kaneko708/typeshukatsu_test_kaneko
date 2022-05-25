def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    left = 0 #探索リストの左端のインデックスを格納
    right = len(sorted_array) - 1 #探索リストの右端のインデックスを格納
    flag = 0 #探索値が見つかった場合に1にする

    while(left <= right):
        #中間の値のインデックスと値を格納
        middle_index = (left + right) // 2 
        middle_value = sorted_array[middle_index]

        #探索する数値が中間の値よりも小さければ,前半部分を探索するためにrightを更新
        if target_number < middle_value:
            right = middle_index - 1
            continue

        #探索する数値が中間の値よりも大きければ,後半部分を探索するためにleftを更新
        if target_number > middle_value:
            left = middle_index + 1
            continue

        #大きくも小さくもない(＝等しい)時にflagを1にしてループを抜ける
        flag = 1
        break

    if(flag == 1):    
      return middle_index

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1