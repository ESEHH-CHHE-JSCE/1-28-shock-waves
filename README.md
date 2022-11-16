# HLLスキームを用いた二次元浅水流モデルの数値解析ソルバー

## 動作環境

Intel Open APIを使って動作確認をしています．環境構築に当たっては例えば下記のページなどが参考になります．

https://qiita.com/Kazutake/items/a069f86d21ca43b6c153

## コードの中身

指定するパラメータについてはコードの中に注釈をつけてあります．Line 330以降を参照ください．

基本的にはこのこの実験水路の条件でしか動作確認は行っておりませんので，条件を変えるとうまく動作しない可能性はあります．

底面凹凸が大きく，水際移動が頻繁に起こる場合などです．

また，このコードは河床変動まで扱えるようにしてあり，流れのみの計算とするために，粒径を大きくして流砂量を小さくし，そのうえで，河床変動の計算は行わないようにしています．その部分を守勢すれば，河床変動の計算も実行できるようにはなります．

## 可視化

計算結果のファイルとして，*.vtk，*.txtの二つが連番で出力されます．

.vtkファイルは，paraview等のソフトで読み込んで可視化することができます．

*.txtファイル
