import os

import boto3
from botocore.exceptions import ClientError
from mastodon import Mastodon


s3 = boto3.resource(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_ACCESS_SECRET'),
)

HOST = 'https://mstdn.fun'


def get_mastodon_instance():
    try:
        with open('pytooter_clientcred.txt', 'wb') as fp:
            s3.Bucket(os.getenv('S3_BUCKET_NAME')).download_fileobj('pytooter_clientcred.txt', fp)
        with open('pytooter_clientcred.txt', 'r') as fp:
            data = fp.read()
        client_id, client_secret = data.split()[0], data.split()[1]
        print('not raised')
    except ClientError:
        client_id, client_secret = Mastodon.create_app(
            'lambda-mstdn-bot-sample',
            api_base_url=HOST
        )
        data = f'{client_id}\n{client_secret}'
        s3.Bucket(os.getenv('S3_BUCKET_NAME')).put_object(Key='pytooter_clientcred.txt', Body=data)
    print(client_id, client_secret)

    mastodon = Mastodon(client_id=client_id, client_secret=client_secret, api_base_url=HOST)
    print(os.getenv('MASTODON_ACCOUNT_EMAIL'))
    print(os.getenv('MASTODON_ACCOUNT_PASSWORD'))
    mastodon.log_in(
        os.getenv('MASTODON_ACCOUNT_EMAIL'),
        os.getenv('MASTODON_ACCOUNT_PASSWORD'),
    )

    return mastodon


def lambda_handler(event, context):
    mastodon = get_mastodon_instance()
    return str(mastodon.timeline_local())


if __name__ == '__main__':
    lambda_handler(None, None)
