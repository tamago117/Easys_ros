# 組み立て手順書

## 内容
- 1. 部品の準備
- 2. 回路部品の作成
- 3. 組み立て
- 4. 浮力の調整
- 5. ソフトウェア準備


## 1. 部品の準備
### 1.1 部品の購入
下記部品リストにある部品を全て購入します（3Dプリントパーツ以外）。

- [部品リスト](https://docs.google.com/spreadsheets/d/1spEkeJp3uywtmMTm2RyMCUT-x4rrJNMb/edit?usp=sharing&ouid=116393592539270427202&rtpof=true&sd=true)


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/764897ff-a218-4242-aec6-9c1a5518aad4" width="50%">


### 1.2 3Dプリントパーツの作成

下記3Dプリンタ部品リストのパーツを印刷します。

- [3Dプリンタ部品リスト](https://docs.google.com/spreadsheets/d/1m-tpGwKx88t4YWLlDcRS2Wr9CotMB-zd/edit?usp=sharing&ouid=116393592539270427202&rtpof=true&sd=true)


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/491e8cb3-8beb-4b62-b75e-d3bc0dcf2273" width="50%">


家庭用サイズのFDM式3Dプリンターを想定しています。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/aeec14bd-fc2d-4e3f-a4ac-ccc087aac8fa" width="50%">


3Dプリントに用いるフィラメントはABSです。

前後のフランジは防水を意識した印刷が必要になります。
印刷設定で構造密度(インフィル)を100%にし、積層スパンを可能な限り細密して印刷します。

## 2. 回路部品の作成

### 2.1  メイン回路



回路図は以下の通りです。


![image](https://github.com/Honazo/Easys_ros/assets/63952012/6487e8e7-12b2-42f7-9a1a-7bbf0cc4ab7e)

実際に組み立てると下の写真のようになります。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/ab8e0a15-5a58-4cfb-ac4f-dfc6b16a2c55" width="50%">

下の画像は3DCAD上で大まかに再現したものです。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/4d56b683-03c3-4a9a-9a16-1bd4bd69a64c" width="50%">



### 2.2 コネクターの接続



#### 2.2.1 ケーブルグランド

耐圧容器の外に出すケーブル(スラスターの3相ケーブル、電源線、LANケーブル)には、あらかじめケーブルグランドを通しておきます。



4台のスラスターの3相ケーブルには3穴のケーブルグランドを、2芯の電源線には1穴のケーブルグランドを通します。

ケーブルグランドにケーブルを通したら、後方フランジの穴にケーブルグランドを固定します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/44abfc17-d6d4-414a-ac50-613bca0fdfa9" width="50%">


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/ae6b3736-ca55-459b-b670-bcd48589ace9" width="50%">


LANケーブルは先端のコネクタが大きくてそのままではケーブルグランドに通りません。
そのため、LANケーブルのコネクタから数cmのところで一旦切断します。
ケーブルグランドに通し、後方フランジの穴にケーブルグランドを固定した後、切断した箇所をはんだ付けして再接続します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/f7571093-308c-4508-bb1f-da3c620806fe" width="50%">


#### 2.2.2 コネクタの接続

ケーブルグランドを固定した後、電源線にはTコネクタ(オス)を装着します。
スラスターの3本線には3相用のコネクタを装着します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/c88c3423-1f0d-49d4-a997-446f27048139" width="50%">


下の写真は回路マウントの1つ目のブロックです。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/2862b783-b833-4fb0-b345-362af9da5a11" width="50%">


Tコネクタ(メス)を6つ並列に配線した基板(電源用+ESC用*4+降圧コンバータ用)と、縦に積んだ4つのESCを横並びに配置し、マウントに固定します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/ff4dc029-8022-4a6c-97c0-8cf0c20adea6" width="50%">


ESCの電源線にはTコネクタを、3相の出力には3相用のコネクタを装着します。

#### 2.2.3 降圧コンバータ回路・サーボコントローラ

降圧コンバータからは下の写真のように配線します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/58ef4fdb-c10f-4b40-b6d4-5685c856a0a8" width="50%">


DC14.8V入力電圧側、DC5V出力電圧側のにそれぞれTコネクタを装着します。

ESCの信号入力線(黒、赤、白、黄の4線)とサーボコントローラの出力端子を接続します。
ESC側の①黒(GND)、②赤(V+)、③白(PWM)をサーボコントローラ側の①黒(GND)、②赤(V+)、③黄(PWM)に接続します。(ESCの黄の線は使いません。)

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/1f69091b-dfed-4536-a566-d70a1b9d513e" width="50%">


#### 2.2.4 Rsapberry Pi 4

降圧コンバータから出力された5V電源とサーボコントローラへの入力(GND,VCC,SCL,SDA)、IMU、Raspberry Pi 4の接続はユニバーサル基板上で配線しています。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/b0a82e16-43a1-4015-979a-24139510946f" width="50%">


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/78a15f1f-3f58-4925-93b2-888858d24fc6" width="50%">

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/29d9651c-d88c-4d59-90ac-f01ac327607f" width="50%">


冒頭の回路図を頼りに製作してください。

Raspberry Pi 4　はケースを着用し、3つ目の回路マウントに接続します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/34269222-ebf4-44c3-9311-b2d6781077a9" width="50%">


最後に、3つの回路マウントと後方フランジをボルトナットで接続します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/9838bbc2-b4cb-4a73-a127-9a512312a104" width="50%">



## 3. 組み立て

### 3.1 スラスター

スラスター底面のハウジングにある3か所の取付穴にインサートナットをはんだこてで熱圧入します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/1861baf3-a66d-47e8-bd0f-77d8b9c01c74" width="50%">



スラスターをスラスターマウントにボルトで固定します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/9d449b39-f9e1-4558-bf7a-0d0c9b0d5007" width="50%">



### 3.2 バッテリーボックス

バッテリーボックス外側底面の4か所の取付穴にインサートナットを熱圧入します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/cf0e0b8e-5965-43d1-888c-ce024883fda2" width="50%">


バッテリーボックスの辺が短い方の側面にΦ12mmの穴を1つあけます。
電動ドリル等を用いて安全に行ってください。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/c2b8aa42-42ae-479f-bc91-e18f2ae1669e" width="50%">



電源線にケーブルグランドを通して、ケーブルグランドをバッテリーボックスに空けた穴に仮締めします。


バッテリーボックス内の電源線の先に、ヒューズ→スイッチ→Tコネクタ(オス)を接続します。

TコネクタでLi-Poバッテリーを接続します。

ボックスに収まることを確認したら、ケーブルグランドを締めます。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/131dc1aa-306c-4710-928e-8c223e7bcd98" width="50%">



ほこりなどを挟んでいないことを十分に注意してバッテリーボックスを閉じます。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/2976fa23-7a3c-416d-972d-06b142818b57" width="50%">



### 3.3 外郭フレーム

上側の外部フレームには6か所、下側の外部フレームには2か所、スラスターマウントを取り付けるためのインサートナット用の下穴があります。
全ての箇所にインサートナットを熱圧入します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/b9db687a-69b1-49b2-9bd0-87d4a1f0876b" width="50%">


バッテリーボックス固定用のマウントに下側外部フレームを接続します。

バッテリーボックス固定用のマウントにバッテリーボックスを接続します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/ba5f1a36-9035-467b-a4fc-b0b332ea0b3c" width="50%">



下側フレームの上にアクリルチューブを乗せます。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/0c108d8d-2c67-4864-868a-f563cd321d0d" width="50%">


上側フレームを下側フレームに接続していきます。
この接続によって上下のフレームが円筒を締め付けることで固定されていきます。
1つずつゆっくりと締め付けてください。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/4be51ae6-f069-40a8-8e53-995b21937de2" width="50%">


### 3.4 耐水容器
前方フランジにアクリル円盤を接着します。アクリルサンデーを用いて、融着させます。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/6c29d233-4286-4bf5-83fa-5abca6695453" width="50%">


アクリルサンデーが固まったら、WEBカメラを前方フランジに固定します。

前方フランジにO-リングをはめます。
O-リングにグリスを塗って滑らかにし、強く引っ張って広げながら少しずつ溝へ持っていきます。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/177c8d3f-0f5c-4415-b293-3c7a2a3a64d7" width="50%">


後方フランジにも同様にしてO-リングをはめます。

WEBカメラのUSBケーブルをラズパイから抜いた状態で、前方フランジをアクリルチューブにはめます。
かなり力が必要です。グリスを使って滑らかにしつつ、はみ出してくるO-リングを中に押し込みながら少しずつ入れていきます。
ほこりなどが挟まらないよう注意してください。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/bd57359c-70d5-411c-982f-d3f0c14ae00a" width="50%">


WEBカメラのUSBケーブルをRaspberry Pi 4に接続します。

後方フランジを前方フランジと同様にしてアクリルチューブにはめます。空気を抜くため、ケーブルグランドを一つだけ緩めておくとよいです。

フランジがはまったらタイラップでフランジと外部フレームを結束し、フランジが抜けないように留めます。

外部フレームにスラスターを固定します。

<img src="https://github.com/Honazo/Easys_ros/assets/63952012/96bebd25-191c-46aa-bda7-a0bcc069f749" width="50%">


## 4. 浮力の調整

密閉出来たら、浴槽などの浅い水槽にロボットを沈めてみます。

何も点けていない状態だと機体の半分以上が水面に浮かびます。

釣り重りを機体外部に少しずつ取り付けていき、4つすべてのスラスタが水中に浸かる程度に重量を調整します。


<img src="https://github.com/Honazo/Easys_ros/assets/63952012/d6c4fd41-da89-4502-bba6-e1e094df7fc8" width="50%">


## 5. ソフトウェア準備

環境構築

Easys_rosのダウンロード



### 5.1 Rasberry pi の準備

機体の電源スイッチを入れる

LANケーブルをPCに接続する

環境構築

### 5.2 ホストPCの準備

ros2の起動

lounch

### 5.3 制御テスト

