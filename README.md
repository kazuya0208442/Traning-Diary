# 🌱&ensp;日本のオリンピック選手育成事業とは？
日本オリンピック委員会と福岡県が協力して、日本の未来を背負うトップアスリートを育成することを目的としています。
１学年およそ30人で編成され、３か月ごとにあらゆるスポーツを経験します。プロの指導者が１人１人を採点し、将来、世界で活躍できるかどうかを見極めます。
 小中学生の期間に種目選択を行い、高校生以降は競技成績に応じて、遠征費の支援、海外リーグ参戦への支援、キャリア支援などの様々なサポートが受けられます。

![hero2-min-min](https://user-images.githubusercontent.com/87218628/162398890-064f4258-acba-4593-8eed-350e4adef300.jpg)

<br>

私の場合は11種目のスポーツを経験させていただきました。

- **小学生**
  - バスケ
  - 水泳
- **中学生**
  - バスケ
  - グラウンドホッケー
  - フェンシング
  - 水球
  - ライフル射撃
  - ウエイトリフティング
  - ボクシング
  - 陸上投擲
 - **高校生**
   - ラグビー(7人制)
   - ラグビー(15人制)
 - **大学生**
   - ラグビー(15人制)

# ⚡️ ご報告
毎年１回、国に競技成績や活動報告をする「報告会」があります。選手の現状を聞いて、どんな支援をするのかを検討することが目的です。
- **2022年3月23日**に、オリンピック選手育成事業の報告書にて、この運動日誌アプリをご提案させて頂きました。
- 上記に加え、「一流アスリートほど子供のころはいろんな競技をしている理由」についての[論文](https://journals.sagepub.com/doi/abs/10.1177/1745691620974772)をスタッフの方に紹介しました。

# 📱 運動日誌アプリ

オリンピック強化選手になると、**運動日誌の提出**が義務付けられます。ただ、いくつか不便な点があります。
### ・記入欄が狭すぎる
### ・字が読み辛い
### ・過去のデータと比較が困難
### ・紛失リスク


<br>


この問題を解決するべく、運動日誌アプリを製作しました。:point_right:  &nbsp;[http://kazuya-portfolio.com](http://kazuya-portfolio.com/)  　


アプリ内の記入例は**当時の私の運動日誌**をそのまま使ってます(^^♪  
<br>

<img src="https://media.giphy.com/media/62rfKf9XfUsNKwnWyo/giphy.gif" width="100%">   

<br>


#  ⚡️ おすすめ機能 
### ・&nbsp;目標にしている選手のプレーが自動で流れます！！


### ・「運動時間」「体幹トレーニング」「睡眠時間」がグラフに！！


### ・&nbsp;レスポンシブ対応！！


<br>

#   :page_facing_up: 実際の運動日誌  


 ### **現在使用されている運動日誌**です。  
 <br>

<img src="https://1.bp.blogspot.com/-3FZ1k9yqBpY/YSsJhBkrKUI/AAAAAAAALX4/kooOBy9ikyQItw8BJdA0jqLyMMAiCnTRgCLcBGAsYHQ/s1754/Jr.%25E6%2597%25A5%25E8%25AA%258C%2B%25E8%25A1%25A8.jpg" width="70%">

### **私の時代の運動日誌**です。 見にくい写真でごめんなさい😢

<img src="https://user-images.githubusercontent.com/87218628/150491732-94782151-2c42-497f-b475-69f65a2287dd.JPG" width="70%">
<!-- <img src="https://user-images.githubusercontent.com/87218628/152968926-8a1f71e5-1149-4e0f-8d17-01aa01be40e6.png" width="70%">   -->

<br>


# 🎨 使用技術  
- Python 3.9.9  
- Django 3.2.11
- PostgreSQL 13.5
- nginx
- Docker / Docker-Compose
- AWS
  - VPC
  - EC2
  - Route53
- HTML
- CSS
- Javascript
- **1人疑似チーム開発 ( GitHub-Flow : issue -> feature branch -> pull request)**  

<br>

# 🛠 Unit Test 
- [YouTube Link を改造する関数](https://github.com/kazuya0208442/Training-Diary/blob/main/app/core/change_link.py)
- [大会までの残り日数を計算する関数](https://github.com/kazuya0208442/Training-Diary/blob/main/app/core/day_computed.py)  　
<br>


# :trident: Infrastructure
![](https://user-images.githubusercontent.com/87218628/145961368-510f1b40-7187-4271-9bb2-2fadcbd43c84.jpg)  
<br>

## ・Nginx (Reverse Proxy) の役割
<!-- バックエンドのアプリケーションサーバーは、同時に処理できるプロセスの数に限界があり(マルチプロセスモデル)、メモリを大量に消費する。本来アプリケーションサーバーは、動的なリクエストを処理するために用意されているものである。したがって、静的ファイルにまで応答しなければならない状況の場合、数に限りのあるプロセスが無駄に消費され、ページ表示の速度が低下し、ユーザー体験の質が落ちてしまう。   -->

バックエンドのアプリケーションサーバーは、同時に処理できるプロセスの数に限界があり(マルチプロセスモデル)、メモリを大量に消費します。本来、アプリケーションサーバーは、動的なリクエストを処理するために用意されているものであり、静的ファイルの配信は得意ではありません。そこで、Reverse Proxy をアプリケーションサーバーの手前に配置することで、静的ファイルはReverse Proxy が担当し、動的なリクエストはアプリケーションサーバーに転送するように設定することで、処理を効率的に行うようにしています。

<!-- この問題を防ぐために、Reverse Proxy をアプリケーションサーバーの手前に配置する。そして静的ファイルなど、アプリケーションサーバーを介さずに応答できるものは Reverse Proxy が直接クライアントに応答し、アプリケーションサーバーでなければ応答できないリクエストのみアプリケーションサーバーに転送する。今回は、「static volume」というvolume を作成し、そこに静的ファイルを配置することで、Reverse Proxy は、静的ファイルを配信できる。   -->
<br>

## :warning: &nbsp; Docker-Compose は本番環境では非推奨
Docker-Compose の欠点は、単一のサーバー上でしか動かせない、ということです。サーバーの負荷が増大し、動的なリソースの割り当てが必要になった場合に対処できません。また、手動でデプロイやアップデートを行わなければならないため、開発コストが余分にかかってしまいます。本来であれば、コンテナ基盤である Amazon ECS などを使用しなければいけませんが、今回は、簡単にデプロイできるというメリットを重視して、Docker-Compose を用いてデプロイしました。

<br>


# :seedling: なぜ開発しようと思ったのですか？  
## １. そもそも、日本のアスリート育成事業ってどんなことをしているのですか？
日本は2004年からオリンピック選手育成事業をスタートしました。小中学生の中で優れた運動能力を持った選手を選抜して、**約10種目のスポーツを専門の指導者の下で訓練し、オリンピック出場に最適な種目を決定**します。私は、グラウンドホッケー、水球、ライフル射撃、フェンシング、円盤投げ、ウエイトリフティング、ラグビー、バスケ、ボクシング、をご指導して頂きました。

<br>

## ２. 運動日誌ってなんですか？

強化選手として選抜された選手は、「運動日誌」を提出する義務があります。「運動日誌」には、毎日のトレーニングメニュー、意識したこと、達成したこと、食事、睡眠時間、体重、体温、など、あらゆる情報を書き込みます。ただ、提出用紙のレイアウトの関係で、記入欄がかなり狭く、びっしりと書き込まれた場合、かなり読み辛いです。スタッフさんは、どんなに小さい文字で書かれてあっても、1行1行丁寧に読み込んで、事細かくアドバイスを返答してくださいます。ただ、この返答の文字もかなり小さくなってしまうという悪循環に陥っています。  

<br>

<!-- スポーツの世界では指導者のアドバイスの一言で、次の試合のプレーが大きく変わるという現象がよく起きます。それくらい、指導者の言葉は重いです。ただ、現状の紙でのやり取りでは、**書きたいアドバイスがあっても、余白が少ないという理由で、断念せざるを得ない**場合もあります。他にも、紙による紛失リスクや、過去のデータの見辛さなど、問題は数多くあります。ただ、これらの問題は全て、オンライン上でやりとりを行うようにすれば解決することです。   -->

## ３. なぜ、運動日誌アプリを作ったのですか？

実は選手の時からずっと「運動日誌」は使いにくい、誰かアプリを作ってほしい、と思っていました。字も読み辛く、動画も貼れない、数値のデータがグラフになるわけでもないので、せっかくのデータがもったいないと思っていました。特に、指導者や監督、コーチのアドバイスは非常に重要で、その一言で、次の試合のプレーがガラッと変わることがよくありますので、そのアドバイスを見辛くしている「紙」のやり取りは撤廃すべきだと思っていました。

ただ、国のスタッフの方達の中でITに詳しい人はかなり少なそうでした。多くの税金を投入して行われている国の取り組みですので、誰かが、内部の活動をDX化するような行動を起こさなければいけません。そこで、自分でアプリを作って、報告会の時に国にURLを送ればいいんじゃないか、と思いまして、プログラミングの勉強を始めました。実際に作ってみると、本当に楽しくて、エンジニアという職業に興味を持つようになり、お仕事としてやってみたいと思うようになりました。世の中にある様々なサービスがどうやって作られているのか、どんなコードで書かれているのか、非常に興味があります。

<!-- 
スタッフの方たちは、**担当になった選手がどうやったらオリンピックに出場できるのか**、そのことを常に考えながら過ごしています。運動日誌の情報を基に、トレーニング計画や食事内容、生活習慣などのアドバイスを行います。私の当時の日誌を上部に添付しておりますが、これだけびっしりと書きこんでしまい、相当見辛いのにもかかわらず、赤ペンでアンダーラインまで引いて、丁寧にアドバイスをしてくださっています。**これだけの熱意をもって、子供たちの指導にあたっているスタッフのためにも、業務を効率化するようなシステムが早くできたらいいなと思っています。**
 -->


<!-- - 日本の**アスリート育成事業のIT化**
  - 競技成績を上げて、**世界を代表するような選手へ**。
  - スタッフの業務効率化により、**子供たちへのサポート**をより強固に。 -->

<br>  

# :sunny: こだわったところ  

## ・&nbsp; 目標としている選手のプレーが自動で流れる！！
<!-- 「YouTube の埋め込みリンク」と「再生開始時間」の２つを入力すると、目標としている選手のプレーが自動で流れます。「YouTube の埋め込みリンク」に、自動再生やミュート、再生開始時間などを表す文字列を挿入することで、YouTube の埋め込みリンクを改造しています。 -->

**自分が日誌を書いていて１番難しかったことは、スポーツの動きを言語化する、という作業でした**。複雑な体の動きを文章で詳細に書こうとすると、どうしても長くなってしまいます。そこで、YouTube などの動画を使って説明するという機能を付けることで、スタッフと選手がよりコミュニケーションを深めることができるのではと考えました。 

<br>

## ・「運動時間」「体幹トレーニング」「睡眠時間」がグラフに！！
オーバートレーニングと呼ばれる、トレーニングをやりすぎて、体の回復が追いついていない状態になる選手が数多くいます。高い目標であればあるほど、もっとトレーニング時間を増やそう、睡眠時間も削って勉強しよう、などと考えてしまう選手も多いです。そこで、毎日の運動時間や睡眠時間を記録することで、自分の適切な運動量や睡眠時間を見積もります。将来的には、心拍変動や体温の変化を常時監視して、異常が起きているときにアラートを飛ばすようにできれば、健康状態を常にベストに保てるのではないかと思っています。特に女性アスリートの場合は、体調管理がかなり重要になってくるので、常時、体調を監視してくれるようなシステムは必要だと思います。

<br>

# :moneybag:  どうやって収益化するのですか？

## ・どこからお金が出ているのか
日本のアスリート育成事業は、文部科学省の下部組織である「スポーツ庁」や「日本オリンピック委員会」「日本スポーツ振興センター」などの組織が主に担当しています。令和４年度の予算はそれぞれ、355億円、140億円、1983億円で合計すると、**２０００億円以上の予算**があります。また、**去年行われた東京オリンピックでは、オリンピックの観客向けのコロナ対策アプリに国は 「７３億１５００万円」の予算を組んでいました。** 以上のことからも分かるように、国のスポーツの予算はかなり潤沢にあり、もしも国のスポーツ事業で使われるようなアプリを開発した場合、表現があまりよろしくないのですが、交渉次第ではかなりの収益が見込めるのではないかと思っています。


<br>

## ・買い切り？ サブスク？
サブスクのメリットは、定期的な収入により収益予測が立ちやすく、どのくらいの金額を開発費に注ぎ込んでいいのか求めることができるという点です。ただし、買い切り型よりも一時的に収益は落ちてしまいますので、いかに継続して課金してもらうかが鍵となります。もし、国に対してサブスクリプション型の契約を結ぶことができるならば、日本がスポーツ事業をやめない限り、半永久的に国から収益を得ることができます。

<br>

## ・スポーツベッティング時代に突入
今、世界ではスポーツベッティングと呼ばれる、オンラインのスポーツカジノサービスが続々と解禁されています。アメリカでは、スポーツベッティングを解禁したことにより、多大な税収が州に入ってきています。日本でも、スポーツベッティングの導入が検討されており、自民党や経済産業省も、「**コロナ後を見据えたスポーツ産業の資金力の強化策**」の提言を行っています。そうなれば、国のスポーツの予算も増えていくのではないかと考えています。

<br>

## ・どこから始めますか？
まずは、オリンピックの強化選手として活動していた「スポーツ科学情報センター」に対して、アスリート育成事業のIT化を提案します。現在も1年に１回、競技成績の報告や OB としての活動を行っていますので、話し合いの場はたくさんあります。今年も３月までに報告書を提出しなければいけませんので、その時に今回のサービスについて提案してみます。国の職員との話し合いの場が設けられた場合、過去に日本のアスリート育成事業を実際に経験し、内部の事情を把握している私のようなエンジニアがいると、アプリ導入への説得も、多少はスムーズに行われるのではないかと考えています。スポーツを引退した身でも、まだ、国のために、将来のトップアスリートになる子供たちのためになるのであれば、頑張りたいと思います。

<br>  

# :tired_face: 難しかったところ & 解決方法  

## ・YouTube 埋め込みタグのランダム文字列に苦労 ...
目標にしている選手のプレーが自動で流れるようにするためには、YouTube の埋め込みリンクに、自動再生やミュート、再生開始時間などを表す文字列を挿入しなければいけません。しかし、動画ごとにランダムに生成される文字列の後ろに挿入する必要があり、場所も真ん中あたりにあるため、どうやってその場所を指定すればいいのか分からなかったです:tired_face:

<br>

## ・文字列の規則性を見つけた！！
YouTube リンクの文字列の中に、何か規則性があるのではないかと思い、たくさんの YouTube リンクを並べて、要素を一つ一つ分解しました。すると、よく見ると、ランダムな文字列の文字数は１１文字で、その前に「embed/」という文字列が必ず存在することが分かりました。そこで、pythonの文字列検索を行い、「embed/」のインデックスを取得し、その１１文字後ろに、指定の文字列をくっつけることで、YouTube リンクの改造に成功しました:blush:

<br>  

# 🎨 なぜその技術を使ったのですか？
## ・Python / Django -> バックエンド言語 / フレームワーク  
Java、Go、Ruby、PHP など、多くのサーバーサイド言語がある中で Python を選んだ理由は「**データ分析によるレコメンド機能**」を将来的に実装したかったからです。そのためには、機械学習や AI 開発のライブラリが豊富なPythonを使用することが、最善であると判断しました。また、Django はデフォルトで、データベースの管理画面を用意してくれているため、管理者用のページを用意する必要がなく、開発の手間が減らせます。

<!-- 選手のトレーニングメニューや食事内容、睡眠時間などを分析し、オリンピック選手になるために必要な情報を選手にレコメンドすることが、この運動日誌アプリが目指しているゴールです。 -->

<br>

## ・uWSGI -> アプリケーションサーバー
webサーバーからのリクエストを受けて、アプリケーションを実行するサーバー。WSGI (Web Server Gateway Interface)とは、Python で記述されたアプリケーションと Webサーバーのプロトコルのことです。他にも、gunicorn の選択肢もありましたが、uWSGI の方が多機能で、RubyやPHPなどにも使用することができるほど汎用性が高いため、uWSGI を選びました。デメリットとしては、設定のパラメータが多いことです。

<br>

## ・Nginx -> Webサーバー
主なWebサーバーの選択肢は、Apache、Nginx です。Apache は、複数のアクセスが急激に発生した場合に、１アクセスに対して１つの対応を行うためサーバー負荷が大きくなり、結果的に処理速度が遅くなったり、最悪の場合にはダウンしてしまうことがあります。Nginx は、複数のアクセスが急激に発生した場合に、内部的に１つの対応として処理することができるため、処理速度が遅くなりにくくサーバーダウンしにくい特徴があります。ただ、今回のアプリは大量アクセスは想定していませんので、どちらの選択肢も魅力としては同じでした。そこで、今回は Django のアプリ制作で使われる頻度の高い Nginx の Web サーバーを選択しました。

<br>

## ・PostgreSQL -> データベースサーバー
主な RDBMS (Relational DataBase Management System) は、Oracle Database、MySQL、SQL Server、PostgreSQL、などが挙げられます。特に、PostgreSQL はオープンソースのデータベースソフトウェアであり、無料で利用可能です。MySQL や Oracle Database と比較すると PostgreSQL は、機能性が劣る部分もありますが、導入コストが低く、エンジニア修行中の私にとっては魅力的でした。また、Django と組み合わせて開発している情報が多く、学習コストが低いところも、初学者にとっては優しいところだと思います。

<br>

## ・Docker / Docker-Compose -> インフラ
エンジニアの方の話では、Docker を使う前までは、チーム全員のPCに同じ開発環境を構築するのは、かなり難しいことだったとお聞きしました。バージョンの違いや、PCにインストールされているプログラムの依存関係などが複雑に絡み合い、開発のスタートラインに立つまでに、かなりの時間を要していたそうです。詳細な手順書を配っても、数人は順番を間違えてしまい、想定外のエラーが出てしまうことも。この問題を解決したのが、Docker です。　　

<br>  

Docker の最大のメリットは、「バージョンの差異や環境の差異をなくして手軽に環境構築ができるようになった」という点です。「Dockerfile」と呼ばれるファイルに「プログラムが動くための依存関係や設定」を書き、コマンドをいくつか打つことで、環境構築ができます。また、従来の仮想化技術のように、ホストOSの上にハードウェアをエミュレートして、ゲストOS を立てる必要もありません。Docker は、ホストのカーネルを共有するため、Docker Engine の上にプロセスが走るだけなのです。これにより、容量が小さくなることで、起動時間が高速になり、開発環境をチームメンバーに配ることも可能になりました。

<br>

また、個人的には、**どんな失敗をしてもいい隔離された環境が手軽に作れる Docker の勉強は、エンジニアとして勉強を続けていく上で、非常に大事なことだと判断しました**。自主トレーニングが好きなだけできる環境って最高だと思います。

<br>

## ・AWS -> クラウドサーバー

主なサーバーの選択肢としては、オンプレミス、レンタルサーバー、VPS (Virtual Private Server)、クラウドサーバー、などが挙げられます。オンプレミスの場合は、自社で用意したサーバーでシステムを運用するため、カスタマイズ性、拡張性、自由度は最も高いです。しかし、初期費用が高く、導入までに数か月かかってしまうため、今回は使いません。レンタルサーバーは、１つの物理サーバーを複数ユーザーで共有するため、他のユーザーの影響を受けやすいという特徴があり、これもあまりよくありません。VPS は１つの仮想サーバー群を個別で利用でき、自由度も比較的高いですが、セキュリティの面や技術者の数などを考慮すると、信頼と実績のあるクラウドサーバーの方が適していると思われます。

<br>

今回のサービスは、「**国のアスリート育成事業を IT 化する**」という趣旨があるため、できるだけ、国の方針に従った方が良いと思われます。日本は政府の情報システムの運用に AWS を採用することを発表しているため、AWS のサービスを利用するのが得策であると考えました。

<br>

## ・Git / GitHub -> バージョン管理システム / ホスティングサービス

<!-- バージョン管理システムとは、ファイルに対して「誰が」「いつ」「何を変更したか」というような情報を記録することで、過去のある時点の状態を復元したり、変更内容の差分を表示できるようにするシステムのことです。 -->

バージョン管理システムは大きく2つに分けられ、「集中管理方式」「分散管理方式」があります。「集中管理方式」の場合、リポジトリが１つだけあり、それに対して複数の開発者がアクセスするため、1人のミスが開発メンバー全員に影響します。一方で、「分散管理方式」の場合、個人のコンピュータ内部に作るローカルリポジトリと複数人で共有するリモートリポジトリの2種類があります。また、変更履歴の流れを枝のように分岐して記録していく「ブランチ」があるため、本番環境に影響を与えずに開発を行うことができます。


<!-- 過去には集中管理方式の「CVS」「Subversion」が多く利用されていましたが、複数人での分散開発の容易さや、パフォーマンスに優れた分散管理方式の「Git」「Mercurial」などがスタンダードになりつつあります。 -->

<br>


<br>

# :bulb: 改善するべき点はありますか？  

## ・データベース設計
まだ、勉強中なのですが、ER図を作ってみました。大きく分類すると「毎日記入する内容」と「毎週記入する内容」の2つがあります。まずは第一正規化により、繰り返している項目を
それぞれ別のレコードとして扱いました。その後、第二正規化により、主キー以外の項目（非キー属性）について、主キーの一部の要素だけで決まる（部分関数従属）ものがあれば別テーブルに分離させました。そして、第三正規化により、主キー以外の項目について項目同士で依存関係を持っているもの（推移的関数従属）も、別テーブルに切り分けました。これにより、非キー属性がすべて主キーに完全関数従属し、なおかつ推移的関数従属性の排除された形式になりました。

<br>

![er_diagram](https://user-images.githubusercontent.com/87218628/157569828-f782a609-1cc9-4332-9b48-d1cdaf330983.png)

<br>


## ・スタッフ側の管理画面の作成
今はまだ、選手側の画面しかできていないため、スタッフ側の管理画面を製作する必要があります。その場合、スタッフは全ての選手の情報を見られるようにしなければいけません。これから、その設計について考えていきたいと思っています。

<br>  



# :hourglass: 開発期間はどれくらいですか？
### 2021年9月 ~ 現在


<br>


# 📖 References  
[Django with Nginx, Gunicorn A Production Ready Solution.](https://medium.com/analytics-vidhya/dajngo-with-nginx-gunicorn-aaf8431dc9e0)  
[How To Deploy Django App with Nginx, Gunicorn, PostgreSQL and Let’s Encrypt SSL on Ubuntu](https://djangocentral.com/deploy-django-with-nginx-gunicorn-postgresql-and-lets-encrypt-ssl-on-ubuntu/)  
[Creating and Deploying a Django Application to AWS](https://www.pulumi.com/blog/deploying-a-django-application-to-aws/)  
[Deploying a Production-ready Django app on AWS](https://dev.to/rmiyazaki6499/deploying-a-production-ready-django-app-on-aws-1pk3)  
[Deploying Django Applications to AWS EC2 with Docker](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)  
[Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  
[Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)  
[Build and Deploy a Django Application using Docker and Compose](https://levelup.gitconnected.com/build-and-deploy-a-django-application-using-docker-and-compose-9bf0d8dc5ebb)  
[DEPOYING DJANGO WITH DOCKER COMPOSE](https://londonappdeveloper.com/deploying-django-with-docker-compose/)  

<br>

# 🌱 印象に残っているスポーツは「水球」
オリンピック選手の育成事業では、10 ~ 12 種目のスポーツを専門の指導者の下で訓練します。各スポーツで指導者から評価が下され、将来的に活躍できる選手になるのかを見極めます。自分にはどのスポーツが適しているのかを、専門家の評価を基にして、客観的に判断することができるので、非常に有意義な時間でした。**特に「水球」を経験したおかげで、「巻き足」と呼ばれる、足がつかない水中での浮き方や泳ぎ方を学びましたので、もし溺れている人を見つけた場合は、助けに入るという選択肢を得ることができました。釣りが趣味ですので、海に落ちる可能性はかなり高いと思いますので、便利な技術を手に入れたなと思いました。**

<br>

- **小学生**
  - バスケ
  - 水泳
- **中学生**
  - バスケ
  - グラウンドホッケー
  - フェンシング
  - 水球
  - ライフル射撃
  - ウエイトリフティング
  - ボクシング
  - 陸上投擲
 - **高校生**
   - ラグビー(7人制)
   - ラグビー(15人制)
 - **大学生**
   - ラグビー(15人制)
 

<br>

# 😄 昔のデータ

<!-- <img src="https://user-images.githubusercontent.com/87218628/162411161-be5cb8cd-b1fe-4cb1-b623-11b7b64a19ae.jpg" width="50%">    -->

<img src="https://user-images.githubusercontent.com/87218628/162406309-1390bc4d-3bf9-4b65-9c4c-a33cfe996c2c.JPG" width="50%">   

<img src="https://user-images.githubusercontent.com/87218628/162406389-6b5ddb6c-af46-41a0-88b8-3a519f34988e.JPG" width="50%">  

<img src="https://user-images.githubusercontent.com/87218628/162406443-ce4504aa-87a4-4a6d-acb1-7758025ed0ce.JPG" width="50%">  

<img src="https://user-images.githubusercontent.com/87218628/162406467-b61d4f76-d437-4123-bf17-888b16d53d56.JPG" width="50%">  

<img src="https://user-images.githubusercontent.com/87218628/162411540-973c26f1-c1a5-4924-ab52-c6c49efeed38.png" width="50%">  

<!-- <img src="https://user-images.githubusercontent.com/87218628/162411492-b460f79c-61b6-4a0d-976a-b8cfd08f6043.JPG" width="50%">   -->

<!-- <img src="https://user-images.githubusercontent.com/87218628/162426111-d48e19c8-0c03-4967-900a-5c9256090e0d.JPG" width="50%">   -->


