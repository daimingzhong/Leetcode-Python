from class1.add import add_function as add_foo




data = 'minist'
data = 'CIFAR'
if data == 'minist':
    from datasets.mnist import MNIST as data
elif data == 'CIFAR':
    from datasets.cifar import CIFAR as data



if __name__ == '__main__':
    f = add_foo(1, 2)
    print(f)