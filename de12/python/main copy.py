score = 0

def display_score():
    print("現在の成績メーター: " + str(score) )

def questsion1():
    global score
    print("初回課題.フィールドワークでわかったことから考察しよう")
    print("A.予想だけで考察する ")
    print("B. 数値をメインとした考察をする")
    print("C. 実際に見て感じたことで考察する")

    choice = input("選択肢を入力してください (A/B/C): ")

    if choice == "A":
        print("道用先生「フィールドワークをもっと生かしましょう。」　成績メーター＋5")
        score += 5
    elif choice == "B":
        print("道用先生「数値に基づいた説得力のあるプレゼンでした。」　成績メーター＋30")
        score += 30 
    elif choice == "C":
        print("道用先生「数値を使ったらもっと良い考察になると思います。」成績メーター＋15")
        score += 15
    display_score()

def questsion2():
    global score
    print("中間課題.3Dプリンターでピンセットをつくる")
    print("A.機能性にこだわる ")
    print("B. ピンセット以外にもいろんな物をつくる")
    print("C. 海外の人のアイデアをもらう")

    choice = input("選択肢を入力してください (A/B/C): ")

    if choice == "A":
        print("道用先生「つかみやすそうな形でおもしろい。」　成績メーター＋15")
        score += 15
    elif choice == "B":
        print("道用先生「積極性があっていいですね。」　成績メーター＋30")
        score += 30 
    elif choice == "C":
        print("道用先生「自分のアイデアで勝負しましょう。」成績メーター＋5")
        score += 5
    display_score()

def questsion3():
    global score
    print("ボーナス課題.外部講師の方の話を聞いてレポートを作成する")
    print("A.参加する ")
    print("B. 友達と遊ぶ")

    choice = input("選択肢を入力してください (A/B): ")

    if choice == "A":
        print("成績メーター＋10")
        score += 10
    elif choice == "B":
        print("成績メーター＋0")
        score += 0 
    display_score()


def add_random_score():
    print("最終課題.レポートの友達審査")
    global score
    import random
    random_score = random.randint(0,50)
    score += random_score 
    print(f"成績メーター＋: + {random_score}")
    display_score()
    

def main():
    print("これは道用先生から単位を獲得するゲームです。課題でもらえる得点で成績メーターをあげましょう。よい成績がもらえるように頑張ってください。")
    name=input("名前を入れてく入れてください")
    questsion1()
    questsion2()
    questsion3()
    add_random_score()
    print("これですべての課題が終了しました。あなたの成績は...")

    if score>=59:
        print(name,"さん、不可") 
    if score<=60 and score>=69:
        print(name,"さん、可")
    if score<=70 and score>=79:
        print(name,"さん、良")
    if score<=80 and score>=89:
        print(name,"さん、優")
    if score<=90:
        print(name,"さん、秀")





if __name__ == "__main__":
    main()
    


