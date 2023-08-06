from aws_recommendation_a2.utils import *


# generate the recommendations for unused cmk
def unused_cmk(self) -> list:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside kms :: unused_cmk()")

    recommendation = []

    client = self.session.client('kms')

    marker = ''
    while True:
        if marker == '':
            response = client.list_keys(
                Limit=1000
            )
        else:
            response = client.list_keys(
                Limit=1000,
                Marker=marker
            )
        for key in response['Keys']:
            key_desc = client.describe_key(
                KeyId=key['KeyId']
            )
            if not key_desc['KeyMetadata']['Enabled']:
                temp = {
                    'Service Name': 'KMS',
                    'Id': key['Keyid'],
                    'Recommendation': 'Remove Customer Master Key',
                    'Description': 'Check for any disabled KMS Customer Master Keys in your AWS account and remove them in order to lower the cost of your monthly AWS bill',
                    'Metadata': {
                        'CreationDate': key_desc['CreationDate'],
                        'Enabled': key_desc['Enabled'],
                        'MultiRegion': key_desc['MultiRegion']
                    },
                    'Recommendation Reason': {
                        'reason': "Customer Master key is not in enabled state"
                    }
                }
                recommendation.append(temp)
        try:
            marker = response['NextMarker']
            if marker == '':
                break
        except KeyError:
            break

    return recommendation
