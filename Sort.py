def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    left = 0  #先頭からの探索で，現在どこにいるかを示す
    right = len(array)-1  #末端からの探索で，現在どこにいるかを示す
    lower_arr = []  #基準値未満のグループを格納する
    higher_arr = []  #基準値以上のグループを格納する
    count = 0  #交換回数を記録し，ソート済みかを判別

    #探索＆交換を行う
    while(1):
        #基準値(pivot)以上の値を探索，基準値以上の値が出るまでleftを進める
        while( array[left] < pivot ):
            left = left+1
            if(left > right):  #すべて基準値未満(leftが末端に到達)なら探索を終了
                break

        #基準値(pivot)未満の値を探索，基準値未満の値が出るまでrightを進める
        while( array[right] >= pivot ):
            right = right-1
            if(right < left):  #すべて基準値以上(rightが先頭に到達)なら探索を終了
                break

        #先頭＆末端からの探索がぶつかったとき交換し，交換回数を記録
        if( left <= right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            count = count+1
        else:
            break
   
    #交換回数(count)が0の時は既にソート済みなので配列を返す  
    if(count == 0):
        return array

    #基準値(pivot)未満のグループと基準値以上のグループに分割する
    for i in range(len(array)):
        if (array[i] < pivot):
            lower_arr.append(array[i])
        else:
            higher_arr.append(array[i])
    
    #各グループに対し，sortを再帰的に使用．空配列の時は再帰しない．
    if(len(lower_arr) >= 1):
        lower_arr = sort(lower_arr)
    if(len(higher_arr) >= 1 ):
        higher_arr = sort(higher_arr)

    return lower_arr + higher_arr

    # ここまで記述

if __name__ == '__main__':
    main()



