# lambda-mstdn-bot-sample
AWS Lambda で動く mastodon bot のサンプル(ただ一言Tootするだけです)

## Packaging
```
./package.sh
```

## Deploy
- 作成したzipファイルをLambdaにアップロード
- 以下の環境変数をそれぞれ設定
  - MASTODON_APPLICATION_NAME
  - MASTODON_ACCOUNT_EMAIL
  - MASTODON_ACCOUNT_PASSWORD
  - S3_BUCKET_NAME (アプリケーションのClientIDとClientSecretを記したファイルを保存するS3 Bucketの名前)
  - TOOT_TEXT (トゥートする内容)
  - DEBUG (これを設定するとトゥートの代わりに内容を標準出力する)
