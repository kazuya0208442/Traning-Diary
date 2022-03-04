# 📱 運動日誌アプリ

オリンピック強化選手になると、**運動日誌の提出**が義務付けられます。ただ、いくつか不便な点があります。
- 記入欄が狭すぎる
- 字が読み辛い
- **過去のデータと比較が困難**
- 紛失リスク


この問題を解決するべく、**運動日誌アプリ**を製作しました。:point_right:  &nbsp;[http://kazuya-portfolio.com](http://kazuya-portfolio.com/)  　


アプリ内の記入例は**当時の私の運動日誌**をそのまま使ってます(^^♪  
<br>

<img src="https://media.giphy.com/media/62rfKf9XfUsNKwnWyo/giphy.gif" width="60%">

#   :page_facing_up: 実際の運動日誌
 ### **現在使用されている運動日誌**です。

<img src="https://1.bp.blogspot.com/-3FZ1k9yqBpY/YSsJhBkrKUI/AAAAAAAALX4/kooOBy9ikyQItw8BJdA0jqLyMMAiCnTRgCLcBGAsYHQ/s1754/Jr.%25E6%2597%25A5%25E8%25AA%258C%2B%25E8%25A1%25A8.jpg" width="70%">

### **私の時代の運動日誌**です。この２枚の写真しか残っていませんでした...😢 見にくい写真でごめんなさい。

<img src="https://user-images.githubusercontent.com/87218628/150491732-94782151-2c42-497f-b475-69f65a2287dd.JPG" width="70%">
<img src="https://user-images.githubusercontent.com/87218628/152968926-8a1f71e5-1149-4e0f-8d17-01aa01be40e6.png" width="70%">


##  ⚡️ おすすめ機能 
- 目標にしている選手のプレーが**自動**で流れます！！


- 「運動時間」「体幹トレーニング」「睡眠時間」が**グラフ**に！！



- **レスポンシブ対応！！**



## 🎨 使用技術  
- Python 3.9.9  
- Django 3.2.11
- PostgreSQL 13.5
- nginx
- Docker / Docker-compose
- AWS
  - VPC
  - EC2
  - Route53
- HTML
- CSS
- Javascript
- **1人疑似チーム開発 ( GitHub-Flow : issue -> feature branch -> pull request)**

## 🛠 Unit Test 
- [YouTube Link を改造する関数](https://github.com/kazuya0208442/Training-Diary/blob/main/app/core/change_link.py)
- [大会までの残り日数を計算する関数](https://github.com/kazuya0208442/Training-Diary/blob/main/app/core/day_computed.py)  　


## :trident: Infrastructure
![](https://user-images.githubusercontent.com/87218628/145961368-510f1b40-7187-4271-9bb2-2fadcbd43c84.jpg)


## :seedling: なぜ作ったの？
日本は**2004年からオリンピック選手育成事業をスタート**しました。小中学生の中で優れた運動能力を持った選手を選抜して、**約10種目のスポーツを専門の指導者の下で訓練し、オリンピック出場に最適な種目を決定**します。私は、グラウンドホッケー、水球、ライフル射撃、フェンシング、円盤投げ、ウエイトリフティング、ラグビー、バスケ、ボクシング、をご指導して頂きました。今でも、貴重な経験として、私の心の中に刻み込まれています。  
<br>

強化選手として選抜された選手は、**「運動日誌」** を提出する義務があります。「運動日誌」には、毎日のトレーニングメニュー、意識したこと、達成したこと、食事、睡眠時間、体重、体温、など、あらゆる情報を書き込みます。ただ、提出用紙のレイアウトの関係で、**記入欄がかなり狭く、びっしりと書き込まれた場合、かなり読み辛い**です。**スタッフさんは、どんなに小さい文字で書かれてあっても、1行1行丁寧に読み込んで、事細かくアドバイスを返答**してくださいます。ただ、この返答の文字もかなり小さくなってしまうという悪循環に陥っています。  

<br>

スポーツの世界では**指導者のアドバイスの一言で、次の試合のプレーが大きく変わる**という現象がよく起きます。それくらい、指導者の言葉は重いです。ただ、現状の紙でのやり取りでは、**書きたいアドバイスがあっても、余白が少ないという理由で、断念せざるを得ない**場合もあります。他にも、紙による紛失リスクや、過去のデータの見辛さなど、問題は数多くあります。ただ、これらの問題は全て、**オンライン上でやりとりを行うようにすれば解決することです**。  

<br>

ですが、**この問題に気付くことができるのは、実際に日の丸をつけている選手か、周りのスタッフの方たちしかいません**。スタッフの方たちはスポーツが専門ですので、なかなかITで問題解決を行うというのは、かなり難しいことだと思います。そこで、**実際に国のアスリート育成事業に参加した私がエンジニアになって、技術的な解決策を提案できれば、お世話になったスタッフさんたちへの恩返しにもつながる**のではないかと思い、この運動日誌アプリを作りました。  

<br>

スタッフの方たちは、**担当になった選手がどうやったらオリンピックに出場できるのか**、そのことを常に考えながら過ごしています。運動日誌の情報を基に、トレーニング計画や食事内容、生活習慣などのアドバイスを行います。私の当時の日誌を上部に添付しておりますが、これだけびっしりと書きこんでしまい、相当見辛いのにもかかわらず、赤ペンでアンダーラインまで引いて、丁寧にアドバイスをしてくださっています。**これだけの熱意をもって、子供たちの指導にあたっているスタッフのためにも、業務を効率化するようなシステムが早くできたらいいなと思っています。**



<!-- - 日本の**アスリート育成事業のIT化**
  - 競技成績を上げて、**世界を代表するような選手へ**。
  - スタッフの業務効率化により、**子供たちへのサポート**をより強固に。 -->


## :sunny: 1番こだわったところ

## :moneybag: 収益化プラン

## :tired_face: 難しかったところ & 解決方法

## 🎨 なぜその技術を使ったの？
- Python / Django  
Java、Go、Ruby、PHP など、多くのサーバーサイド言語がある中で Python を選んだ理由は「**データ分析によるレコメンド機能**」を将来的に実装したかったからです。選手のトレーニングメニューや食事内容、睡眠時間などを分析し、**オリンピック選手になるために必要な情報を選手にレコメンド**することが、この運動日誌アプリが目指しているゴールです。そのためには、**機械学習やAI開発のライブラリが豊富なPython**を使用することが、最善であると判断しました。

- uwsgi
- nginx
- PostgreSQL
- Docker / Docker-compose
- AWS

## :hourglass: 開発期間
2021年9月 ~ 現在

## :bulb: 改善するべき点

## 📖 References  
[Django with Nginx, Gunicorn A Production Ready Solution.](https://medium.com/analytics-vidhya/dajngo-with-nginx-gunicorn-aaf8431dc9e0)  
[How To Deploy Django App with Nginx, Gunicorn, PostgreSQL and Let’s Encrypt SSL on Ubuntu](https://djangocentral.com/deploy-django-with-nginx-gunicorn-postgresql-and-lets-encrypt-ssl-on-ubuntu/)  
[Creating and Deploying a Django Application to AWS](https://www.pulumi.com/blog/deploying-a-django-application-to-aws/)  
[Deploying a Production-ready Django app on AWS](https://dev.to/rmiyazaki6499/deploying-a-production-ready-django-app-on-aws-1pk3)  
[Deploying Django Applications to AWS EC2 with Docker](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)  
[Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  
[Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)  
[Build and Deploy a Django Application using Docker and Compose](https://levelup.gitconnected.com/build-and-deploy-a-django-application-using-docker-and-compose-9bf0d8dc5ebb)  
[DEPOYING DJANGO WITH DOCKER COMPOSE](https://londonappdeveloper.com/deploying-django-with-docker-compose/)  
add udemy...


