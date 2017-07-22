import requests


def test_lottery(n):
    num_1 = 0
    num_2 = 0
    num_5 = 0
    num_vip = 0
    post_url = "http://localhost/Train.OrderProcess/api/json/\
            CalculateAcceleratePackage"
    for x in range(1, n):
        post_data = {"ordernum": "123456"}
        result = requests.post(post_url, json=post_data)
        data = result.json()
        area = data['Table_Num']

        # check the value
        if area in ['B', 'C', 'G']:
            num_1 += 1
        elif area in ['D', 'F', 'H']:
            num_2 += 1
        elif area in ['A', 'I']:
            num_5 += 1
        else:
            num_vip += 1


if __name__ == '__main__':
    num = int(input('please enter the number...'))
    test_lottery(num)
    print('test ok...')
