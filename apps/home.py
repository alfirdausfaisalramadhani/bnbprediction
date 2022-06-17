import streamlit as st
from PIL import Image

def app():

    st.subheader('SEJARAH BINANCE COIN')
    
    image = Image.open('logo.png')
    st.image(image, caption='')
    
    st.write('Diluncurkan pertama kali pada 26 Juni hingga 3 Juli 2017 dalam jaringan blockchain Ethereum, BNB memiliki harga penawarannya perdana sebesar 1 ETH untuk 2.700 BNB atau 1 BTC untuk 20.000 BNB.')
    st.write('Kendati ditawarkan perdana dalam ICO, aset digital ini tidak mengklaim sebagai produk investasi ataupun trading. Menurut pengembangnya, BNB adalah alat tukar yang digunakan untuk pembayaran, utamanya di platform yang berada dalam lingkup Binance, seperti binance.com, Binance DEX, Binance Chain, dan aplikasi di atas Binance Smart Chain.')
    st.write('Ketika ICO, sebanyak 10% atau 20 juta BNB dijual kepada angel investor. Apasih angel investor? Angel investor adalah sebutan untuk investor yang membiayai start up di awal pendiriannya. Lalu, sebanyak 40% atau 80 juta BNB diperuntukkan bagi tim, sementara sisanya atau 50% dari total suplai BNB atau sebanyak 100 juta koin lagi, dilepas ke pasar.')
    st.write('Adapun dana yang dihimpun dari ICO tersebut dipakai untuk membangun platform Binance dan menutup biaya operasional. Diketahui, sebanyak 30% dari total dana juga digunakan untuk membangun brand dan memasarkan BNB. Strategi ini terbukti sukses sebab terhitung 11 hari setelah penawaran perdananya, Binance telah memiliki platform sendiri.')
    
    
    st.subheader('SIAPAKAH PENDIRI BNB COIN?')
    
    image = Image.open('cz.jpg')
    st.image(image, caption='')
    
    st.write('Nama Changpeng Zhao atau lebih dikenal dengan panggilan CZ merupakan salah satu tokoh dalam dunia kripto yang namanya tersorot sebagai pendiri sekaligus CEO Binance.')
    st.write('Bagi sebagian orang, nama Changpeng Zhao mungkin asing di telinga. Namun bagi kalangan investor dan pemain di dunia kripto, CZ adalah sosok yang fenomenal karena mampu melejitkan Binance dalam hitungan minggu.')
    st.write('Forbes mencatatkan kekayaan yang dimiliki CZ per Juni 2021 adalah sebesar US$1,9 miliar. Angka fantastis ini ia dapatkan berkat Binance, bursa pertukaran uang kripto yang ia dirikan pada tahun 2017.')
    st.write('CZ juga dikenal karena kesuksesannya mengembangkan uang digital dalam kurun waktu 180 hari. Siapa sangka, ia mampu meraih kesuksesan itu hanya dari sebuah ruangan sempit.')
    st.write('Sebelum berada ada titik kesuksesannya saat ini, ia bahkan sempat menjual apartemennya di Shanghai. Meskipun ia telah masuk dalam daftar orang kaya baru yang dirilis Forbes, Cia dikenal sebagai sosok yang hidup tanpa memamerkan kemewahan.')
    
    st.subheader('APA ITU BNB COIN?')
    
    image = Image.open('apaitubnb.jpg')
    st.image(image, caption='')
    
    st.write('BNB saat ini dirilis dalam tiga format. Di samping ERP-20 dalam Ethereum blockchain, BNB pun terbit dalam juga BEP-2 dan BEP-20 yang merupakan koin “asli” dalam jaringan Binance chain dan Binance smart chain.')
    st.write('Kendati begitu, suplai BNB dibatasi sebanyak maksimal 200 juta koin saja. Alasannya adalah  selaku pengembang BNB, Binance diketahui secara berkala melakukan pemusnahan terhadap suplai BNB untuk menjamin pasokannya tidak terlalu banyak.')
    st.write('Adapun pemusnahan atau yang disebut sebagai burning ini dilakukan Binance tiap 3 bulan dengan membeli BNB senilai 20% keuntungan perusahaan. Kemudian, koin yang sudah dibeli itu dimusnahkan dalam jaringan blockchain sehingga transaksinya transparan.')    
    st.write('Mengingat aksi ini terus dilakukan secara berkala, suplai BNB saat ini hanya ada 153,432,897 di dunia. Jumlah itu boleh jadi akan terus susut sehingga membuat kelangkaan untuk menjaga valuasinya tetap berharga.')
    
    st.subheader('Penggunaan BNB COIN')
    
    image = Image.open('penggunaanbnb.jpg')
    st.image(image, caption='')
    
    st.write('Seperti dijelaskan di atas, BNB diperkenalkan sebagai alat tukar alih-alih instrumen investasi. Akan tetapi, pada akhirnya, bagaimana BNB digunakan kembali kepada para selaku penggunanya.')
    st.write('Menurut klaim pihak Binance, jutaan BNB sudah digunakan untuk membiayai perjalanan dan membeli cindera mata virtual. BNB pun bisa dapat dalam pinjaman, sebagai hadiah, untuk membuat smart contracts, serta transaksi-transaksi lainnya.')
    st.write('Adapun sebanyak 2 juta pengguna BNB menggunakan koin tersebut untuk membiayai 127 miliar trading. Untuk total transaksi dengan BNB untuk membayar fee trading ini saja sudah sekitar 40 juta BNB atau 20% dari total suplai BNB.')
    st.write('Trading yang bisa dibiayai dengan BNB ini berlangsung pada platform Binance.com, Binance DEX, dan Binance Chain. Untuk diketahui, membayar fee trading dengan BNB cukup populer karena Binance mengenakan diskon bagi pengguna yang membayar fee dengan BNB.')
    st.write('Standar fee trading di Binance, yakni sebesar 0,1%, yang dapat dibayar juga dengan aset yang Anda miliki apabila Anda tidak berminat mengejar diskon fee. Di samping efektif digunakan untuk membayar fee trading, aset digital yang satu ini juga menjadi nyawa dari Binance DEX dalam rantai Binance. Di samping itu, ribuan aplikasi dalam Binance Smart Chain (BSC) pun diketahui bergantung pada token BNB.')
    
    
    st.subheader('Cara kerja BNB COIN')
    
    image = Image.open('carakerja.jpg')
    st.image(image, caption='')
    
    st.write('BNB coin ini pada awalnya dimulai sebagai salah satu token ERC-20 tradisional di jaringan Ethereum. Lantas, Binance akhirnya memperkenalkan blockchain-nya sendiri.')
    st.write('Koin yang dikeluarkan dari blockchain Binance ini bakal diamankan oleh mekanisme konsensus Bizantine-fault-tolerant (BFT) Tendermint. Token ERC-20 menggunakan konsensus proof-of-stake (PoS), yang memungkinkan perhitungan sangat terukur pembuatan smart contract.')
    st.write('Lain halnya dari PoS, mekanisme BFT dari blockchain Binance ini tidak mendukung fungsi untuk pembuatan smart contract.')
    
    
    st.subheader('Keunggulan BNB COIN')
    
    image = Image.open('keunggulanbnb.jpg')
    st.image(image, caption='')
    
    st.write('Binance sudah berkembang sebagai platform exchange kripto terbesar dengan kantor cabang di beberapa negara. Adapun organisasi sampingan Binance pun memiliki daya tarik yang signifikan. Tentu saja, hal itu akan memperkuat fundamental dari BNB coin.')
    st.write('Keunggulan dari BNB coin, salah satunya, adalah dorongan terhadap pengembangannya. Binance pada mulanya hanya untuk trading kripto, tetapi sekarang perusahaan itu sudah memperbanyak layanannya di sejumlah bidang.')
    st.write('Binance diketahui telah berhasil mengalami meningkatkan minat investor terhadap cryptocurrency sejak merilis BNB coin. Pada awal tahun ini, harga BNB coin mengalami kenaikan yang signifikan dan memecahkan rekor All-Time High-nya (ATH).')
    st.write('Menurut banyak pengamat aset kripto, mereka yakin bahwa harga BNB coin bakal terus meningkat dan kembali memecahkan rekor ATH sebelumnya. Hal itu sendiri tidak terlepas dari kepopuleran BNB coin sebagai salah satu aset kripto dengan market cap terbesar saat ini.')