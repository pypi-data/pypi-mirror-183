def IMG_create_Conv_Net(x_train, y_train, x_val, y_val, IMG_WIDTH = 64, IMG_HEIGHT = 64, num_channels = 3, pretrained_yes_no = 1, 
                        pretrained_model_list = ['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge'], 
                        pretrained_model_type = 7, CLASS_COUNT = 10,
                        max_conv2D_units = 9, max_conv2D_kernel = 5, second_Conv2D_block = 1, third_Conv2D_block = 1, if_maxpooling = 1, max_Maxpooling_size = 3, activation_func = 4, 
                        аctivation_list = ['softmax','sigmoid','linear','relu','tanh'], padding_type = 1,
                        paddingType_list = ["same", "same"], if_dropout = 1, flatten_globalMax_globalAveragePool = 2, if_batchnorm = 1, second_dense =  1, third_dense = 1, dense_size = 7, 
                        dense_activation = 4, denseActivation_list = ['softmax','sigmoid','linear','relu','tanh'], optimizer_type = 7, 
                        optimizer_type_list = ['SGD', 'RMSprop', 'Adam', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl'],
                        dense_batchnorm = 1, dense_dropout = 1, ep= 10, verb = 1, n = 20, nsurv = 10, epohs = 5, times_for_popul = 5, best_models_num = 3, 
                        link = '/content/drive/MyDrive/GA_folder', worst_models_num = 3):

  import random as random                          # Генератор рандомных чисел
  from keras.optimizers import Adam                    # Оптимизатор Adam
  from tensorflow.keras.models import Sequential   # Сеть прямого распространения
  from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, GlobalAveragePooling2D, GlobalMaxPooling2D, Lambda, Resizing
  from google.colab import files                   # Для загрузки своей картинки
  import numpy as np                               # Библиотека работы с массивами
  import time                                      # Для подсчета времени
  from statistics import mean                      # Для подсчета среднего значения
  import gdown                                     # Подключение модуля для загрузки данных из облака
  import tensorflow
  import pandas as pd

  def createRandomNet():
    
    net = [] 
    net.append(random.randint(0,1))                     # Делаем или нет нормализацию первым слоем        net[0]
    net.append(random.randint(4,max_conv2D_units))      # Первый свёрточный слой от 16 до 512 нейронов    net[1]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро первого свёрточного слоя от 2 до 5         net[2]
    net.append(random.randint(0,activation_func))       # Функция активации первого слоя                  net[3]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling в первом блоке             net[4]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling в первом блоке                net[5]

    net.append(random.randint(0,second_Conv2D_block))   # Делаем ли второй сверточный блок                net[6]
    net.append(random.randint(4,max_conv2D_units))      # Второй свёрточный слой от 16 до 512 нейронов    net[7]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро второго свёрточного слоя от 3 до 5         net[8]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling во втором блоке            net[9]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling во втором блоке               net[10]
    net.append(random.randint(0,activation_func))       # Функция активации второго слоя                  net[11]

    net.append(random.randint(0,third_Conv2D_block))    # Делаем ли третий сверточный блок                net[12]
    net.append(random.randint(4,max_conv2D_units))      # Третий свёрточный слой от 16 до 512 нейронов    net[13]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро третьего свёрточного слоя от 2 до 5        net[14]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling в третьем блоке            net[15]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling в третьем блоке               net[16]
    net.append(random.randint(0,activation_func))       # Функция активации третьего слоя                 net[17]

    net.append(random.randint(0,dense_activation))      # Функция активации первого dense слоя            net[18]
    net.append(random.randint(0,2))                     # Функция активации последнего слоя               net[19]

    net.append(random.randint(0,flatten_globalMax_globalAveragePool)) # тестируем Flatten, GlobalMax и GlobalAveragePoo net[20]
    net.append(random.randint(4,dense_size))            # Размер полносвязного слоя от 16 до 64           net[21]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout в первом блоке                net[22]
    net.append(random.randint(0,4))                     # Процент Dropout в первом блоке                  net[23]

    net.append(random.randint(0,1))                     # Тестируем ли функции активации                  net[24]
    net.append(random.randint(0,1))                     # Активация последнего слоя - sigmoid или softmax net[25]
    net.append(random.randint(0,padding_type))          # Тип padding - same или valid для 1 слоя 1 блока net[26]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout во втором блоке               net[27]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout в третьем блоке               net[28]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию в первом блоке           net[29]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию во втором блоке          net[30]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию в третьем блоке          net[31]
    net.append(random.randint(0,4))                     # Процент Dropout во втором блоке                 net[32]
    net.append(random.randint(0,4))                     # Процент Dropout в третьем блоке                 net[33]
    net.append(random.randint(0,padding_type))          # Какой padding используем для 1 слоя 2 блока     net[34]
    net.append(random.randint(0,padding_type))          # Какой padding используем для 1 слоя 3 блока     net[35]

    net.append(random.randint(0,1))                     # Делаем ли в первом блоке второй слой Conv2D     net[36]
    net.append(random.randint(0,1))                     # Делаем ли в первом блоке третий слой Conv2D     net[37]
    net.append(random.randint(0,1))                     # Делаем ли во втором блоке второй слой Conv2D    net[38]
    net.append(random.randint(0,1))                     # Делаем ли во втором блоке третий слой Conv2D    net[39]
    net.append(random.randint(0,1))                     # Делаем ли в третьем блоке второй слой Conv2D    net[40]
    net.append(random.randint(0,1))                     # Делаем ли в третьем блоке третий слой Conv2D    net[41]

    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D в первом блоке     net[42]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D в первом блоке    net[43]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D во втором блоке    net[44]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D во втором блоке   net[45]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D в третьем блоке    net[46]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D в третьем блоке   net[47]

    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя в первом блоке     net[48]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя в первом блоке    net[49]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя во втором блоке    net[50]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя во втором блоке   net[51]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя в третьем блоке    net[52]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя в третьем блоке   net[53]

    net.append(random.randint(0,activation_func))      # Функция активации второго слоя первого блока     net[54]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя первого блока    net[55]
    net.append(random.randint(0,activation_func))      # Функция активации второго слоя второго блока     net[56]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя второго блока    net[57]
    net.append(random.randint(0,activation_func))      # Функция активации второго слоя третьего блока    net[58]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя третьего блока   net[59]

    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя первого блока      net[60]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя первого блока     net[61]
    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя второго блока      net[62]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя второго блока     net[63]
    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя третьего блока     net[64]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя третьего блока    net[65]

    net.append(random.randint(0,second_dense))          # Делаем ли второй полносвязный слой               net[66]
    net.append(random.randint(0,third_dense))           # Делаем ли третий полносвязный слой               net[67]
    net.append(random.randint(4,dense_size))            # Размер второго полносвязного слоя                net[68]
    net.append(random.randint(4,dense_size))            # Размер третьего полносвязного слоя               net[69]
    net.append(random.randint(0,dense_activation))      # Функция активации второго полносвязного слоя     net[70]
    net.append(random.randint(0,dense_activation))      # Функция активации третьего полносвязного слоя    net[71]

    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после первого dense       net[72]
    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после второго dense       net[73]
    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после третьего dense      net[74]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после первого dense            net[75]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после второго dense            net[76]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после третьего dense           net[77]
    net.append(random.randint(0,4))                     # Процент Dropout после первого dense              net[78]
    net.append(random.randint(0,4))                     # Процент Dropout после второго dense              net[79]
    net.append(random.randint(0,4))                     # Процент Dropout после третьего dense             net[80]
    net.append(random.randint(0,pretrained_yes_no))     # Применяем ли предобученные модели                net[81]
    net.append(random.randint(0,pretrained_model_type)) # Какую из предобученных моделей применяем         net[82]
    net.append(random.randint(0,optimizer_type))        # Какой optimizer применяем                        net[83]
    return net
  def createConvNet(net):

    model = Sequential()             # Создаем модель Sequential
    
    makeFirstNormalization = net[0]  # Делаем ли нормализацию в начале

    firstConvSize = 2 ** net[1]      # Размер первого свёрточного слоя
    firstConvKernel = net[2]         # Ядро первого свёрточного слоя
    firstActivation0 = net[3]        # Функция активации первого слоя первого блока
    firstPaddingType0 = net[26]      # Какой padding используем для 1 слоя 1 блока - same или valid
    makeFirstConv1 = net[36]         # Делаем ли в первом блоке второй слой Conv2D
    firstConvSize1 = 2 ** net[42]    # Размер свертки второго Conv2D в первом блоке
    firstConvKernel1 = net[48]       # Ядро второго свёрточного слоя в первом блоке
    firstPaddingType1 = net[60]      # Тип паддинга для второго слоя первого блока
    firstActivation1 = net[54]       # Функция активации второго слоя первого блока
    makeFirstConv2 = net[37]         # Делаем ли в первом блоке третий слой Conv2D
    firstConvSize2 = 2 ** net[43]    # Размер свертки третьего Conv2D в первом блоке
    firstConvKernel2 = net[49]       # Ядро третьего свёрточного слоя в первом блоке
    firstPaddingType2 = net[61]      # Тип паддинга для третьего слоя первого блока
    firstActivation2 = net[55]       # Функция активации третьего слоя первого блока
    makeMaxPooling0 = net[4]         # Делаем ли maxpooling для первого блока
    maxPoolingSize0 = net[5]         # Размер MaxPooling
    droppout0 = net[22]              # Делаем ли Dropout в первом блоке
    dropout_size0 = net[23]          # Процент Dropout в первом блоке
    batchnorm0 = net[29]             # делаем ли нормализацию после первого блока
    makeSecondConv = net[6]          # Делаем ли второй свёрточный слой
    secondConvSize = 2 ** net[7]     # Размер второго свёрточного слоя
    secondConvKernel = net[8]        # Ядро второго свёрточного слоя
    secondPaddingType0 = net[34]     # Какой padding используем для 1 слоя 2 блока - same или valid
    secondActivation0 = net[11]      # Функция активации для первого слоя второго блока
    makeSecondConv1 = net[38]        # Делаем ли во втором блоке второй слой Conv2D
    secondConvSize1 = 2 ** net[44]   # Размер свертки второго Conv2D во втором блоке
    secondConvKernel1 = net[50]      # Ядро второго свёрточного слоя во втором блоке
    secondPaddingType1 = net[62]     # Тип паддинга для второго слоя второго блока
    secondActivation1 = net[56]      # Функция активации второго слоя второго блока
    makeSecondConv2 = net[39]        # Делаем ли во втором блоке третий слой Conv2D
    secondConvSize2 = 2 ** net[45]   # Размер свертки третьего Conv2D во втором блоке
    secondConvKernel2 = net[51]      # Ядро третьего свёрточного слоя во втором блоке
    secondPaddingType2 = net[63]     # Тип паддинга для третьего слоя второго блока
    secondActivation2 = net[57]      # Функция активации третьего слоя второго блока
    makeMaxPooling1 = net[9]         # Делаем ли MaxPooling во втором блоке
    maxPoolingSize1 = net[10]        # Размер MaxPooling во втором блоке
    droppout1 = net[27]              # Dropout во втором блоке
    dropout_size1 = net[32]          # Процент Dropout во втором блоке
    batchnorm1 = net[30]             # делаем ли нормализацию после второго блока

    makeThirdConv = net[12]          # Делаем ли третий свёрточный слой
    thirdConvSize = 2 ** net[13]     # Размер третьего свёрточного слоя
    thirdConvKernel = net[14]        # Ядро третьего свёрточного слоя
    thirdPaddingType0 = net[35]      # Какой padding используем для 1 слоя 3 блока - same или valid
    thirdActivation0 = net[17]       # Функция активации для первого слоя третьего блока
    makeThirdConv1 = net[40]         # Делаем ли в третьем блоке второй слой Conv2D
    thirdConvSize1 = 2 ** net[46]    # Размер свертки второго Conv2D в третьем блоке
    thirdConvKernel1 = net[52]       # Ядро второго свёрточного слоя в третьем блоке
    thirdPaddingType1 = net[64]      # Тип паддинга для второго слоя третьего блока
    thirdActivation1 = net[58]       # Функция активации второго слоя третьего блока
    makeThirdConv2 = net[41]         # Делаем ли в третьем блоке третий слой Conv2D
    thirdConvSize2 = 2 ** net[47]    # Размер свертки третьего Conv2D в третьем блоке
    thirdConvKernel2 = net[53]       # Ядро третьего свёрточного слоя в третьем блоке
    thirdPaddingType2 = net[65]      # Тип паддинга для третьего слоя третьего блока
    thirdActivation2 = net[59]       # Функция активации третьего слоя третьего блока
    makeMaxPooling2 = net[15]        # Делаем ли MaxPooling в третьем блоке
    maxPoolingSize2 = net[16]        # Размер MaxPooling в третьем блоке
    droppout2 = net[28]              # Делаем ли Dropout в третьем блоке
    dropout_size2 = net[33]          # Процент Dropout в третьем блоке
    batchnorm2 = net[31]             # делаем ли нормализацию после третьего блока
    
    activation3 = net[18]                                                   # Функция активации для предпоследнего dense слоя
    activation4 = net[19]                                                   # Функция активации для последнего слоя
    flat_globMax_globAver = net[20]                                         # тестируем Flatten, GlobalMaxPooling2D или GlobalAveragePooling2D

    denseSize = 2 ** net[21]                                                # Размер первого полносвязного слоя
    secondDense = net[66]                                                   # Создание второго полносвязного слоя
    thirdDense = net[67]                                                    # Создание третьего полносвязного слоя
    
    secondDenseSize = 2 ** net[68]                                          # Размер второго полносвязного слоя
    thirdDenseSize = 2 ** net[69]                                           # Размер третьего полносвязного слоя
    secondDenseActivation = net[70]                                           # какие функции активации тестируем во втором полносвязном слое
    thirdDenseActivation = net[71]                                            # какие функции активации тестируем в третьем полносвязном слое

    firstDenseBatchnorm = net[72]                                             # делаем ли нормализацию после первого полносвязного слоя
    secondDenseBatchnorm = net[73]                                            # делаем ли нормализацию после второго полносвязного слоя
    thirdDenseBatchnorm = net[74]                                             # делаем ли нормализацию после третьего полносвязного слоя

    firstDenseDropout = net[75]                                               # делаем ли Dropout после первого полносвязного слоя
    secondDenseDropout = net[76]                                              # делаем ли Dropout после второго полносвязного слоя
    thirdDenseDropout = net[77]                                               # делаем ли Dropout после третьего полносвязного слоя

    firstDenseDropoutSize = net[78]                                           # процент Dropout после первого полносвязного слоя
    secondDenseDropoutSize = net[79]                                          # процент Dropout после второго полносвязного слоя
    thirdDenseDropoutSize = net[80]                                           # процент Dropout после третьего полносвязного слоя
    
    test_activations = net[24]       # Тестируем ли функции активации - в моменте не используется
    final_activation = net[25]       # Какие активации тестируем на последнем слое - sigmoid или softmax
    final_activation_list = ['softmax','sigmoid']                     # какие функции активации тестируем в последнем полносвязном слое
    dropout_list = [0.05, 0.1, 0.3, 0.4, 0.5]
    #flat_globMax_globAver_list = [Flatten, GlobalMaxPooling2D, GlobalAveragePooling2D] # тестируем Flatten, GlobalMaxPooling2D или GlobalAveragePooling2D

    use_pretrained_model = net[81]                                            # Используем ли предобученные модели
    pretrained_model_name = net[82]                                           # Название предобученной модели
    #pretrained_model_list= [NASNetMobile, ResNet50, ResNet50V2, VGG16, VGG19, Xception, EfficientNet, NASNetLarge]
    optimizer_type = net[83]                                                  # Какой optimizer применяем
    # Если не используем предобученные модели:
    if (use_pretrained_model==0):

      # Если делаем нормализацию вначале
      if (makeFirstNormalization!=0):   

        # Добавляем слой BatchNormalization
        model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels))) 
        model.add(Conv2D(firstConvSize, firstConvKernel, activation=аctivation_list[firstActivation0], padding=paddingType_list[firstPaddingType0])) 
      else:
      # если не делаем нормализацию в начале
        model.add(Conv2D(firstConvSize, firstConvKernel, input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels), activation=аctivation_list[firstActivation0], padding=paddingType_list[firstPaddingType0]))
      # делаем ли второй сверточный слой
      if makeFirstConv1!=0:
        model.add(Conv2D(firstConvSize1, firstConvKernel1, activation=аctivation_list[firstActivation1], padding=paddingType_list[firstPaddingType1]))
      # делаем ли третий сверточный слой
      if makeFirstConv2!=0:
        model.add(Conv2D(firstConvSize2, firstConvKernel2, activation=аctivation_list[firstActivation2], padding=paddingType_list[firstPaddingType2]))

      if makeMaxPooling0!=0:            # Если делаем maxpooling
        model.add(MaxPooling2D(maxPoolingSize0))

      if (batchnorm0!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization()) # Добавляем слой BatchNormalization 

      if (droppout0!=0):                 # Если добавляем Dropout в первый блок
        model.add(Dropout(dropout_list[dropout_size0]))         

      if (makeSecondConv!=0):           # Если делаем второй свёрточный слой
        # Добавляем Conv2D-слой с secondConvSize нейронами и ядром (secondConvKernel)
        model.add(Conv2D(secondConvSize, secondConvKernel, activation=аctivation_list[secondActivation0], padding=paddingType_list[secondPaddingType0]))  
        # делаем ли второй сверточный слой
      if makeSecondConv1!=0:
        model.add(Conv2D(secondConvSize1, secondConvKernel1, activation=аctivation_list[secondActivation1], padding=paddingType_list[secondPaddingType1]))
      # делаем ли третий сверточный слой
      if makeSecondConv2!=0:
        model.add(Conv2D(secondConvSize2, secondConvKernel2, activation=аctivation_list[secondActivation2], padding=paddingType_list[secondPaddingType2]))
    
      if (makeMaxPooling1!=0):        # Если делаем MaxPooling
      # Добавляем слой MaxPooling2D с размером (maxPoolingSize)
        model.add(MaxPooling2D(pool_size=maxPoolingSize1)) 

      if (batchnorm1!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 

      if (droppout1!=0):                 # Если добавляем Dropout во второй блок
        model.add(Dropout(dropout_list[dropout_size1]))   
          
      if (makeThirdConv!=0):            # Если делаем третий свёрточный слой
      # Добавляем Conv2D-слой с thirdConvSize нейронами и ядром (thirdConvKernel)
        model.add(Conv2D(thirdConvSize, thirdConvKernel, activation=аctivation_list[thirdActivation0], padding=paddingType_list[thirdPaddingType0]))
      # делаем ли второй сверточный слой
      if makeThirdConv1!=0:
        model.add(Conv2D(thirdConvSize1, thirdConvKernel1, activation=аctivation_list[thirdActivation1], padding=paddingType_list[thirdPaddingType1]))
      # делаем ли третий сверточный слой
      if makeThirdConv2!=0:
        model.add(Conv2D(thirdConvSize2, thirdConvKernel2, activation=аctivation_list[thirdActivation2], padding=paddingType_list[thirdPaddingType2]))
      if (makeMaxPooling2!=0):        # Если делаем MaxPooling
      # Добавляем слой MaxPooling2D с размером (maxPoolingSize, maxPoolingSize)
        model.add(MaxPooling2D(pool_size=maxPoolingSize2)) 
      if (batchnorm2!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if (droppout2!=0):                 # Если добавляем Dropout в первый блок
        model.add(Dropout(dropout_list[dropout_size2]))   
      if flat_globMax_globAver==0:
        model.add(Flatten())                         # Добавляем слой Flatten
      elif flat_globMax_globAver==1:
        model.add(GlobalMaxPooling2D())              # Добавляем слой GlobalMaxPooling2D
      else:
        model.add(GlobalAveragePooling2D())          # Добавляем слой GlobalAveragePooling2D
    #['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge']  
    # если используем предобученные модели
    else:
      if (makeFirstNormalization!=0):   
        # Добавляем слой BatchNormalization
        model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels))) 
        # NASNetMobile
        if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
          nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))
          model.add(Resizing(224, 224, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_conv)
        # ResNet50
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
          resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet50_conv.layers:
            layer.trainable=False
          preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input
          model.add(Lambda(preprocess_input_resnet50, name='preprocessing'))
          model.add(resnet50_conv)
        # ResNet50V2
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
          resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet_v2_conv.layers:
            layer.trainable=False
          preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input
          model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing'))
          model.add(resnet_v2_conv)
        # VGG16
        elif pretrained_model_list[pretrained_model_name] == 'VGG16':
          vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg16_conv.layers:
            layer.trainable=False
          preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input
          model.add(Lambda(preprocess_input_vgg16, name='preprocessing'))
          model.add(vgg16_conv)
        # VGG19
        elif pretrained_model_list[pretrained_model_name] == 'VGG19':
          vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg19_conv.layers:
            layer.trainable=False
          preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input
          model.add(Lambda(preprocess_input_vgg19, name='preprocessing'))
          model.add(vgg19_conv)
        # Xception
        elif pretrained_model_list[pretrained_model_name] == 'Xception':
          xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in xception_conv.layers:
            layer.trainable=False
          preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input
          model.add(Lambda(preprocess_input_xception, name='preprocessing'))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(xception_conv)
        # EfficientNet
        elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
          efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in efficientnet_conv.layers:
            layer.trainable=False
          preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input
          model.add(Lambda(preprocess_input_efficientnet, name='preprocessing'))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(efficientnet_conv)
        # NASNetLarge
        elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
          nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_large_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))
          model.add(Resizing(331, 331, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_large_conv)
      # Если не делаем Batchnormalization
      else:
        if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
          nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(224, 224, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_conv)

        elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
          resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet50_conv.layers:
            layer.trainable=False
          preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input
          model.add(Lambda(preprocess_input_resnet50, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(resnet50_conv)
        # ResNet50V2
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
          resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet_v2_conv.layers:
            layer.trainable=False
          preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input
          model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(resnet_v2_conv)
        # VGG16
        elif pretrained_model_list[pretrained_model_name] == 'VGG16':
          vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg16_conv.layers:
            layer.trainable=False
          preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input
          model.add(Lambda(preprocess_input_vgg16, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(vgg16_conv)
        # VGG19
        elif pretrained_model_list[pretrained_model_name] == 'VGG19':
          vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg19_conv.layers:
            layer.trainable=False
          preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input
          model.add(Lambda(preprocess_input_vgg19, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(vgg19_conv)
        # Xception
        elif pretrained_model_list[pretrained_model_name] == 'Xception':
          xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in xception_conv.layers:
            layer.trainable=False
          preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input
          model.add(Lambda(preprocess_input_xception, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(xception_conv)
        # EfficientNet
        elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
          efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in efficientnet_conv.layers:
            layer.trainable=False
          preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input
          model.add(Lambda(preprocess_input_efficientnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(efficientnet_conv)
        # NASNetLarge
        elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
          nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_large_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(331, 331, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_large_conv)

    
      model.add(Flatten())                         # Добавляем слой Flatten

    # Добавляем слой Dense с denseSize нейронами
    model.add(Dense(denseSize, activation=denseActivation_list[activation3]))
    if firstDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
      model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
    if firstDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
      model.add(Dropout(dropout_list[firstDenseDropoutSize]))

    if secondDense!=0:
      # Добавляем слой Dense с denseSize нейронами
      model.add(Dense(secondDenseSize, activation=denseActivation_list[secondDenseActivation]))
      if secondDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if secondDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
        model.add(Dropout(dropout_list[secondDenseDropoutSize]))


    if thirdDense!=0:
      # Добавляем слой Dense с denseSize нейронами
      model.add(Dense(thirdDenseSize, activation=denseActivation_list[thirdDenseActivation]))
      if thirdDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if thirdDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
        model.add(Dropout(dropout_list[thirdDenseDropoutSize]))


    # Добавляем Dense-слой с softmax  или sigmoid-активацией и 3 нейронами
    model.add(Dense(CLASS_COUNT, activation=final_activation_list[final_activation])) 
    
    return model                      # Возвращаем модель
  def evaluateNet(net, ep, verb):
    # если используем не предобученную модель, то батчсайз =64
    if (net[81]==0):
      b_size=64
    # если используем предобученную модель, то батчсайз зависит от модели
    else:
      if pretrained_model_list[net[82]]=='NASNetMobile' or pretrained_model_list[net[82]]=='ResNet50' or pretrained_model_list[net[82]]=='ResNet50V2' or pretrained_model_list[net[82]]=='VGG16' or pretrained_model_list[net[82]]=='VGG19':
        b_size=64
      else:
        b_size=8
    if CLASS_COUNT==2:
      loss_func = 'binary_crossentropy'
    else:
      loss_func = 'categorical_crossentropy'
    val = 0
    time.time()
    model = createConvNet(net) # Создаем модель createConvNet
    opt_type = net[83]
    
    optimizer=optimizer_type_list[opt_type]

    # Компилируем сеть
    model.compile(loss=loss_func, optimizer=optimizer, metrics=['accuracy'])

    # Обучаем сеть на данных с фото водителей
    history = model.fit(x_train, 
                        y_train, 
                        batch_size=b_size, 
                        epochs=ep,
                        validation_split=0.1,
                        verbose=verb)
      
    val = history.history["val_accuracy"][-1] # Возвращаем точность на проверочной выборке с последней эпохи
    return val, model  

  nnew = n - nsurv    # Количество новых (столько новых ботов создается)
  l = 84              # Размер бота
  mut = 0.01          # Коэффициент мутаций
  
  worst_models_num = 3# Сколько худших моделей мы хотим получить по итогам всех запусков
  popul = []          # Массив популяции
  val = []            # Одномерный массив значений точности этих ботов
  mean_val = []       # Массив со средними точностями по запускам
  max_val = []        # Массив с лучшими точностями по запускам
  best_models  =[]    # 3 лучших модели по итогам всех запусков
  worst_models = []   # 3 худших модели по итогам всех запусков

  from google.colab import drive
  import os.path
  from os import path
  drive.mount('/content/drive')
  
  if path.exists(link) == False:
    os.mkdir(link)
  # Создаём случайных ботов
  for i in range(n):
    popul.append(createRandomNet())
    
  for it in range(epohs):                 # Пробегаем по всем запускам генетики
    #val = []                             # список с точностями ботов на проверочной выборке с последней эпохи
    curr_time = time.time()
    curr_models=[[] for _ in range(n)]    # список с моделями из данного запуска
    bots_accuracy_list = [[] for _ in range(n)] # создаем список с n пустыми списками под точности бота

    # для каждого бота создается список, в который будут добавляться точности на каждом запуске:
    
    for j in range(times_for_popul):
      for i in range(n):                    # Пробегаем в цикле по всем ботам 
        bot = popul[i]                      # Берем очередного бота
        f, model_sum = evaluateNet(bot, ep, verb) # Вычисляем точность текущего бота на последней эпохе и получаем обученную модель
        #val.append(f)                       # Добавляем полученное значение в список val
        bots_accuracy_list[i].append(f)
        curr_models[i].append(model_sum)       # Добавляем текущую модель в список с моделями curr_models
    best_bots_accuracy_list = []            # список из лучших точностей по каждому боту
    for acc in bots_accuracy_list:
      best_bots_accuracy_list.append(max(acc))

    #best_curr_models = []
    sval = sorted(best_bots_accuracy_list, reverse=1)         # Сортируем best_bots_accuracy_list по убыванию точности

    # Получаем индексы ботов из списка по убыванию точности в данном запуске генетики sval:
    indexes_best = []
    for i in range(len(sval)):
      indexes_best.append(best_bots_accuracy_list.index(sval[i]))

    # Получаем список моделей по ботам
    models_curr_list = []
    for i in curr_models:
      models_curr_list.append(i[0])

    # Получаем отсортированный список моделей по убыванию точности
    best_models = []
    for i in indexes_best:
      best_models.append(models_curr_list[i])

    ind_best = indexes_best[0]                                # Индекс лучшего бота в популяции
    ind_worst = indexes_best[-1]                              # Индекс худшего бота в популяции
    worst_val = sorted(best_bots_accuracy_list, reverse=0)    # Сортируем best_bots_accuracy_list по возрастанию точности
    
    current_mean_val = mean(best_bots_accuracy_list)          # Средняя точность ботов на каждом запуске по кол-ву запусков
    current_max_val = max(best_bots_accuracy_list)            # Лучшая из лучших точностей ботов на каждом запуске по кол-ву запусков
    mean_val.append(current_mean_val)
    max_val.append(current_max_val)
    # сохраняем текущую популяцию ботов и их лучшую аккураси по итогам всех запусков одной популяции на гугл драйв
    bots_accuracy_df = pd.DataFrame(
      {'bots': popul,
      'accuracy': best_bots_accuracy_list
      })
    base_filename = 'bots_accuracy_df.csv'
    os.path.join(link, base_filename)
    bots_accuracy_df.to_csv(os.path.join(link, base_filename), index=False)
    final_best_bot = popul[ind_best]
    
    # Выводим точность 
    print("запуск номер ", (int(it)+1), " Секунд на запуск: ", int(time.time() - curr_time), " лучший бот - ", final_best_bot) 
    print(" Средняя точность ботов на последней эпохе ", current_mean_val,  "худший бот в данном запуске: ", popul[ind_worst])
    print(" Лучшая точность ботов на последней эпохе ", current_max_val)
    print("model_summary лучшей модели ", best_models[0].summary(), "model_summary худшей модели ", best_models[-1].summary()) 
    
    newpopul = []                         # Создаем пустой список под новую популяцию
    for i in range(nsurv):                # Пробегаем по всем выжившим ботам
      index = best_bots_accuracy_list.index(sval[i])          # Получаем индекс очередного бота из списка лучших в списке val
      newpopul.append(popul[index])       # Добавляем в новую популяцию бота из popul с индексом index
      
    for i in range(nnew):                 # Проходимся в цикле nnew-раз  
      indexp1 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
      indexp2 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
      botp1 = newpopul[indexp1]           # Получаем первого бота-родителя по indexp1
      botp2 = newpopul[indexp2]           # Получаем второго бота-родителя по indexp2    
      newbot = []                         # Создаем пустой список под значения нового бота    
      net4Mut = createRandomNet()         # Создаем случайную сеть для мутаций
      for j in range(l):                  # Пробегаем по всей длине размерности (84)      
        x = 0      
        pindex = random.random()          # Получаем случайное число в диапазоне от 0 до 1

        # Если pindex меньше 0.5, то берем значения от первого бота, иначе от второго
        if pindex < 0.5:
          x = botp1[j]
        else:
          x = botp2[j]
        
        # С вероятностью mut устанавливаем значение бота из net4Mut
        if (random.random() < mut):
          x = net4Mut[j]
          
        newbot.append(x)                  # Добавляем очередное значение в нового бота      
      newpopul.append(newbot)             # Добавляем бота в новую популяцию      
    popul = newpopul                      # Записываем в popul новую посчитанную популяцию

  final_best_models = []
  for i in range(best_models_num):        # Пробегаем по всем моделям из последнего запуска
    index = best_bots_accuracy_list.index(sval[i])            # Получаем индекс модели из списка лучших в списке best_bots_accuracy_list
    final_best_models.append(best_models[index])# Добавляем в best_models модель с индексом index

  for i in range(worst_models_num):        # Пробегаем по всем моделям из последнего запуска
    index = best_bots_accuracy_list.index(worst_val[i])        # Получаем индекс модели из списка худших в списке val
    worst_models.append(best_models[index])# Добавляем в worst_models модель с индексом index
  return mean_val, max_val, final_best_models, final_best_bot  # Получаем среднее и максимальное значение аккураси на проверочной выборке, набор из n лучших моделей, лучший бот на последнем запуске

def visualize_mean_accuracy(mean_val, max_val):
  import matplotlib.pyplot as plt
  # Создание полотна для рисунка
  plt.figure(1, figsize=(8, 10))

  plt.plot(mean_val, label='Среднее значение точности на проверочной выборке')
  plt.plot(max_val, label='Лучшее значение точности на проверочной выборке')
  # Задание подписей осей 
  plt.xlabel('Эпоха обучения')
  plt.ylabel('Значение точности')
  plt.legend()

  # Фиксация графиков и рисование всей картинки
  plt.show()

'''
Функция восстановления обучения
из сохраненных ботов и их аккураси
link = '/content/drive/MyDrive/GA_folder' - адрес папки в Google Drive, куда будем сохранять ботов и их accuracy
base_filename = 'bots_accuracy_df.csv' - имя файла

'''

def Recovery_Conv_Net(x_train, y_train, x_val, y_val, IMG_WIDTH = 64, IMG_HEIGHT = 64, num_channels = 3, pretrained_yes_no = 1, 
                        pretrained_model_list = ['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge'], 
                        pretrained_model_type = 7, CLASS_COUNT = 10,
                        max_conv2D_units = 9, max_conv2D_kernel = 5, second_Conv2D_block = 1, third_Conv2D_block = 1, if_maxpooling = 1, max_Maxpooling_size = 3, activation_func = 4, 
                        аctivation_list = ['softmax','sigmoid','linear','relu','tanh'], padding_type = 1,
                        paddingType_list = ["same", "same"], if_dropout = 1, flatten_globalMax_globalAveragePool = 2, if_batchnorm = 1, second_dense =  1, third_dense = 1, dense_size = 7, 
                        dense_activation = 4, denseActivation_list = ['softmax','sigmoid','linear','relu','tanh'], optimizer_type = 7, 
                        optimizer_type_list = ['SGD', 'RMSprop', 'Adam', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl'],
                        dense_batchnorm = 1, dense_dropout = 1, ep= 10, verb = 1, n = 20, nsurv = 10, epohs = 5, times_for_popul = 5, best_models_num = 3, 
                        link = '/content/drive/MyDrive/GA_folder', worst_models_num = 3):

  import random as random                          # Генератор рандомных чисел
  from keras.optimizers import Adam                    # Оптимизатор Adam
  from tensorflow.keras.models import Sequential   # Сеть прямого распространения
  from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, GlobalAveragePooling2D, GlobalMaxPooling2D, Lambda, Resizing
  from google.colab import files                   # Для загрузки своей картинки
  import numpy as np                               # Библиотека работы с массивами
  import time                                      # Для подсчета времени
  from statistics import mean                      # Для подсчета среднего значения
  import gdown                                     # Подключение модуля для загрузки данных из облака
  import tensorflow
  import pandas as pd

  def createRandomNet():
    
    net = [] 
    net.append(random.randint(0,1))                     # Делаем или нет нормализацию первым слоем        net[0]
    net.append(random.randint(4,max_conv2D_units))      # Первый свёрточный слой от 16 до 512 нейронов    net[1]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро первого свёрточного слоя от 2 до 5         net[2]
    net.append(random.randint(0,activation_func))       # Функция активации первого слоя                  net[3]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling в первом блоке             net[4]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling в первом блоке                net[5]

    net.append(random.randint(0,second_Conv2D_block))   # Делаем ли второй сверточный блок                net[6]
    net.append(random.randint(4,max_conv2D_units))      # Второй свёрточный слой от 16 до 512 нейронов    net[7]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро второго свёрточного слоя от 3 до 5         net[8]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling во втором блоке            net[9]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling во втором блоке               net[10]
    net.append(random.randint(0,activation_func))       # Функция активации второго слоя                  net[11]

    net.append(random.randint(0,third_Conv2D_block))    # Делаем ли третий сверточный блок                net[12]
    net.append(random.randint(4,max_conv2D_units))      # Третий свёрточный слой от 16 до 512 нейронов    net[13]
    net.append(random.randint(2,max_conv2D_kernel))     # Ядро третьего свёрточного слоя от 2 до 5        net[14]
    net.append(random.randint(0,if_maxpooling))         # Делаем ли MaxPooling в третьем блоке            net[15]
    net.append(random.randint(2,max_Maxpooling_size))   # Размер MaxPooling в третьем блоке               net[16]
    net.append(random.randint(0,activation_func))       # Функция активации третьего слоя                 net[17]

    net.append(random.randint(0,dense_activation))      # Функция активации первого dense слоя            net[18]
    net.append(random.randint(0,2))                     # Функция активации последнего слоя               net[19]

    net.append(random.randint(0,flatten_globalMax_globalAveragePool)) # тестируем Flatten, GlobalMax и GlobalAveragePoo net[20]
    net.append(random.randint(4,dense_size))            # Размер полносвязного слоя от 16 до 64           net[21]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout в первом блоке                net[22]
    net.append(random.randint(0,4))                     # Процент Dropout в первом блоке                  net[23]

    net.append(random.randint(0,1))                     # Тестируем ли функции активации                  net[24]
    net.append(random.randint(0,1))                     # Активация последнего слоя - sigmoid или softmax net[25]
    net.append(random.randint(0,padding_type))          # Тип padding - same или valid для 1 слоя 1 блока net[26]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout во втором блоке               net[27]
    net.append(random.randint(0,if_dropout))            # Делаем ли Dropout в третьем блоке               net[28]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию в первом блоке           net[29]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию во втором блоке          net[30]
    net.append(random.randint(0,if_batchnorm))          # Делаем ли нормализацию в третьем блоке          net[31]
    net.append(random.randint(0,4))                     # Процент Dropout во втором блоке                 net[32]
    net.append(random.randint(0,4))                     # Процент Dropout в третьем блоке                 net[33]
    net.append(random.randint(0,padding_type))          # Какой padding используем для 1 слоя 2 блока     net[34]
    net.append(random.randint(0,padding_type))          # Какой padding используем для 1 слоя 3 блока     net[35]

    net.append(random.randint(0,1))                     # Делаем ли в первом блоке второй слой Conv2D     net[36]
    net.append(random.randint(0,1))                     # Делаем ли в первом блоке третий слой Conv2D     net[37]
    net.append(random.randint(0,1))                     # Делаем ли во втором блоке второй слой Conv2D    net[38]
    net.append(random.randint(0,1))                     # Делаем ли во втором блоке третий слой Conv2D    net[39]
    net.append(random.randint(0,1))                     # Делаем ли в третьем блоке второй слой Conv2D    net[40]
    net.append(random.randint(0,1))                     # Делаем ли в третьем блоке третий слой Conv2D    net[41]

    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D в первом блоке     net[42]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D в первом блоке    net[43]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D во втором блоке    net[44]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D во втором блоке   net[45]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки второго Conv2D в третьем блоке    net[46]
    net.append(random.randint(4,max_conv2D_units))     # Размер свертки третьего Conv2D в третьем блоке   net[47]

    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя в первом блоке     net[48]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя в первом блоке    net[49]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя во втором блоке    net[50]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя во втором блоке   net[51]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро второго свёрточного слоя в третьем блоке    net[52]
    net.append(random.randint(2,max_conv2D_kernel))    # Ядро третьего свёрточного слоя в третьем блоке   net[53]

    net.append(random.randint(0,activation_func))      # Функция активации второго слоя первого блока     net[54]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя первого блока    net[55]
    net.append(random.randint(0,activation_func))      # Функция активации второго слоя второго блока     net[56]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя второго блока    net[57]
    net.append(random.randint(0,activation_func))      # Функция активации второго слоя третьего блока    net[58]
    net.append(random.randint(0,activation_func))      # Функция активации третьего слоя третьего блока   net[59]

    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя первого блока      net[60]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя первого блока     net[61]
    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя второго блока      net[62]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя второго блока     net[63]
    net.append(random.randint(0,padding_type))         # Тип паддинга для второго слоя третьего блока     net[64]
    net.append(random.randint(0,padding_type))         # Тип паддинга для третьего слоя третьего блока    net[65]

    net.append(random.randint(0,second_dense))          # Делаем ли второй полносвязный слой               net[66]
    net.append(random.randint(0,third_dense))           # Делаем ли третий полносвязный слой               net[67]
    net.append(random.randint(4,dense_size))            # Размер второго полносвязного слоя                net[68]
    net.append(random.randint(4,dense_size))            # Размер третьего полносвязного слоя               net[69]
    net.append(random.randint(0,dense_activation))      # Функция активации второго полносвязного слоя     net[70]
    net.append(random.randint(0,dense_activation))      # Функция активации третьего полносвязного слоя    net[71]

    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после первого dense       net[72]
    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после второго dense       net[73]
    net.append(random.randint(0,dense_batchnorm))       # Делаем ли нормализацию после третьего dense      net[74]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после первого dense            net[75]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после второго dense            net[76]
    net.append(random.randint(0,dense_dropout))         # Делаем ли Dropout после третьего dense           net[77]
    net.append(random.randint(0,4))                     # Процент Dropout после первого dense              net[78]
    net.append(random.randint(0,4))                     # Процент Dropout после второго dense              net[79]
    net.append(random.randint(0,4))                     # Процент Dropout после третьего dense             net[80]
    net.append(random.randint(0,pretrained_yes_no))     # Применяем ли предобученные модели                net[81]
    net.append(random.randint(0,pretrained_model_type)) # Какую из предобученных моделей применяем         net[82]
    net.append(random.randint(0,optimizer_type))        # Какой optimizer применяем                        net[83]
    return net
  def createConvNet(net):

    model = Sequential()             # Создаем модель Sequential
    
    makeFirstNormalization = net[0]  # Делаем ли нормализацию в начале

    firstConvSize = 2 ** net[1]      # Размер первого свёрточного слоя
    firstConvKernel = net[2]         # Ядро первого свёрточного слоя
    firstActivation0 = net[3]        # Функция активации первого слоя первого блока
    firstPaddingType0 = net[26]      # Какой padding используем для 1 слоя 1 блока - same или valid
    makeFirstConv1 = net[36]         # Делаем ли в первом блоке второй слой Conv2D
    firstConvSize1 = 2 ** net[42]    # Размер свертки второго Conv2D в первом блоке
    firstConvKernel1 = net[48]       # Ядро второго свёрточного слоя в первом блоке
    firstPaddingType1 = net[60]      # Тип паддинга для второго слоя первого блока
    firstActivation1 = net[54]       # Функция активации второго слоя первого блока
    makeFirstConv2 = net[37]         # Делаем ли в первом блоке третий слой Conv2D
    firstConvSize2 = 2 ** net[43]    # Размер свертки третьего Conv2D в первом блоке
    firstConvKernel2 = net[49]       # Ядро третьего свёрточного слоя в первом блоке
    firstPaddingType2 = net[61]      # Тип паддинга для третьего слоя первого блока
    firstActivation2 = net[55]       # Функция активации третьего слоя первого блока
    makeMaxPooling0 = net[4]         # Делаем ли maxpooling для первого блока
    maxPoolingSize0 = net[5]         # Размер MaxPooling
    droppout0 = net[22]              # Делаем ли Dropout в первом блоке
    dropout_size0 = net[23]          # Процент Dropout в первом блоке
    batchnorm0 = net[29]             # делаем ли нормализацию после первого блока
    makeSecondConv = net[6]          # Делаем ли второй свёрточный слой
    secondConvSize = 2 ** net[7]     # Размер второго свёрточного слоя
    secondConvKernel = net[8]        # Ядро второго свёрточного слоя
    secondPaddingType0 = net[34]     # Какой padding используем для 1 слоя 2 блока - same или valid
    secondActivation0 = net[11]      # Функция активации для первого слоя второго блока
    makeSecondConv1 = net[38]        # Делаем ли во втором блоке второй слой Conv2D
    secondConvSize1 = 2 ** net[44]   # Размер свертки второго Conv2D во втором блоке
    secondConvKernel1 = net[50]      # Ядро второго свёрточного слоя во втором блоке
    secondPaddingType1 = net[62]     # Тип паддинга для второго слоя второго блока
    secondActivation1 = net[56]      # Функция активации второго слоя второго блока
    makeSecondConv2 = net[39]        # Делаем ли во втором блоке третий слой Conv2D
    secondConvSize2 = 2 ** net[45]   # Размер свертки третьего Conv2D во втором блоке
    secondConvKernel2 = net[51]      # Ядро третьего свёрточного слоя во втором блоке
    secondPaddingType2 = net[63]     # Тип паддинга для третьего слоя второго блока
    secondActivation2 = net[57]      # Функция активации третьего слоя второго блока
    makeMaxPooling1 = net[9]         # Делаем ли MaxPooling во втором блоке
    maxPoolingSize1 = net[10]        # Размер MaxPooling во втором блоке
    droppout1 = net[27]              # Dropout во втором блоке
    dropout_size1 = net[32]          # Процент Dropout во втором блоке
    batchnorm1 = net[30]             # делаем ли нормализацию после второго блока

    makeThirdConv = net[12]          # Делаем ли третий свёрточный слой
    thirdConvSize = 2 ** net[13]     # Размер третьего свёрточного слоя
    thirdConvKernel = net[14]        # Ядро третьего свёрточного слоя
    thirdPaddingType0 = net[35]      # Какой padding используем для 1 слоя 3 блока - same или valid
    thirdActivation0 = net[17]       # Функция активации для первого слоя третьего блока
    makeThirdConv1 = net[40]         # Делаем ли в третьем блоке второй слой Conv2D
    thirdConvSize1 = 2 ** net[46]    # Размер свертки второго Conv2D в третьем блоке
    thirdConvKernel1 = net[52]       # Ядро второго свёрточного слоя в третьем блоке
    thirdPaddingType1 = net[64]      # Тип паддинга для второго слоя третьего блока
    thirdActivation1 = net[58]       # Функция активации второго слоя третьего блока
    makeThirdConv2 = net[41]         # Делаем ли в третьем блоке третий слой Conv2D
    thirdConvSize2 = 2 ** net[47]    # Размер свертки третьего Conv2D в третьем блоке
    thirdConvKernel2 = net[53]       # Ядро третьего свёрточного слоя в третьем блоке
    thirdPaddingType2 = net[65]      # Тип паддинга для третьего слоя третьего блока
    thirdActivation2 = net[59]       # Функция активации третьего слоя третьего блока
    makeMaxPooling2 = net[15]        # Делаем ли MaxPooling в третьем блоке
    maxPoolingSize2 = net[16]        # Размер MaxPooling в третьем блоке
    droppout2 = net[28]              # Делаем ли Dropout в третьем блоке
    dropout_size2 = net[33]          # Процент Dropout в третьем блоке
    batchnorm2 = net[31]             # делаем ли нормализацию после третьего блока
    
    activation3 = net[18]                                                   # Функция активации для предпоследнего dense слоя
    activation4 = net[19]                                                   # Функция активации для последнего слоя
    flat_globMax_globAver = net[20]                                         # тестируем Flatten, GlobalMaxPooling2D или GlobalAveragePooling2D

    denseSize = 2 ** net[21]                                                # Размер первого полносвязного слоя
    secondDense = net[66]                                                   # Создание второго полносвязного слоя
    thirdDense = net[67]                                                    # Создание третьего полносвязного слоя
    
    secondDenseSize = 2 ** net[68]                                          # Размер второго полносвязного слоя
    thirdDenseSize = 2 ** net[69]                                           # Размер третьего полносвязного слоя
    secondDenseActivation = net[70]                                           # какие функции активации тестируем во втором полносвязном слое
    thirdDenseActivation = net[71]                                            # какие функции активации тестируем в третьем полносвязном слое

    firstDenseBatchnorm = net[72]                                             # делаем ли нормализацию после первого полносвязного слоя
    secondDenseBatchnorm = net[73]                                            # делаем ли нормализацию после второго полносвязного слоя
    thirdDenseBatchnorm = net[74]                                             # делаем ли нормализацию после третьего полносвязного слоя

    firstDenseDropout = net[75]                                               # делаем ли Dropout после первого полносвязного слоя
    secondDenseDropout = net[76]                                              # делаем ли Dropout после второго полносвязного слоя
    thirdDenseDropout = net[77]                                               # делаем ли Dropout после третьего полносвязного слоя

    firstDenseDropoutSize = net[78]                                           # процент Dropout после первого полносвязного слоя
    secondDenseDropoutSize = net[79]                                          # процент Dropout после второго полносвязного слоя
    thirdDenseDropoutSize = net[80]                                           # процент Dropout после третьего полносвязного слоя
    
    test_activations = net[24]       # Тестируем ли функции активации - в моменте не используется
    final_activation = net[25]       # Какие активации тестируем на последнем слое - sigmoid или softmax
    final_activation_list = ['softmax','sigmoid']                     # какие функции активации тестируем в последнем полносвязном слое
    dropout_list = [0.05, 0.1, 0.3, 0.4, 0.5]
    #flat_globMax_globAver_list = [Flatten, GlobalMaxPooling2D, GlobalAveragePooling2D] # тестируем Flatten, GlobalMaxPooling2D или GlobalAveragePooling2D

    use_pretrained_model = net[81]                                            # Используем ли предобученные модели
    pretrained_model_name = net[82]                                           # Название предобученной модели
    #pretrained_model_list= [NASNetMobile, ResNet50, ResNet50V2, VGG16, VGG19, Xception, EfficientNet, NASNetLarge]
    optimizer_type = net[83]                                                  # Какой optimizer применяем
    # Если не используем предобученные модели:
    if (use_pretrained_model==0):

      # Если делаем нормализацию вначале
      if (makeFirstNormalization!=0):   

        # Добавляем слой BatchNormalization
        model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels))) 
        model.add(Conv2D(firstConvSize, firstConvKernel, activation=аctivation_list[firstActivation0], padding=paddingType_list[firstPaddingType0])) 
      else:
      # если не делаем нормализацию в начале
        model.add(Conv2D(firstConvSize, firstConvKernel, input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels), activation=аctivation_list[firstActivation0], padding=paddingType_list[firstPaddingType0]))
      # делаем ли второй сверточный слой
      if makeFirstConv1!=0:
        model.add(Conv2D(firstConvSize1, firstConvKernel1, activation=аctivation_list[firstActivation1], padding=paddingType_list[firstPaddingType1]))
      # делаем ли третий сверточный слой
      if makeFirstConv2!=0:
        model.add(Conv2D(firstConvSize2, firstConvKernel2, activation=аctivation_list[firstActivation2], padding=paddingType_list[firstPaddingType2]))

      if makeMaxPooling0!=0:            # Если делаем maxpooling
        model.add(MaxPooling2D(maxPoolingSize0))

      if (batchnorm0!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization()) # Добавляем слой BatchNormalization 

      if (droppout0!=0):                 # Если добавляем Dropout в первый блок
        model.add(Dropout(dropout_list[dropout_size0]))         

      if (makeSecondConv!=0):           # Если делаем второй свёрточный слой
        # Добавляем Conv2D-слой с secondConvSize нейронами и ядром (secondConvKernel)
        model.add(Conv2D(secondConvSize, secondConvKernel, activation=аctivation_list[secondActivation0], padding=paddingType_list[secondPaddingType0]))  
        # делаем ли второй сверточный слой
      if makeSecondConv1!=0:
        model.add(Conv2D(secondConvSize1, secondConvKernel1, activation=аctivation_list[secondActivation1], padding=paddingType_list[secondPaddingType1]))
      # делаем ли третий сверточный слой
      if makeSecondConv2!=0:
        model.add(Conv2D(secondConvSize2, secondConvKernel2, activation=аctivation_list[secondActivation2], padding=paddingType_list[secondPaddingType2]))
    
      if (makeMaxPooling1!=0):        # Если делаем MaxPooling
      # Добавляем слой MaxPooling2D с размером (maxPoolingSize)
        model.add(MaxPooling2D(pool_size=maxPoolingSize1)) 

      if (batchnorm1!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 

      if (droppout1!=0):                 # Если добавляем Dropout во второй блок
        model.add(Dropout(dropout_list[dropout_size1]))   
          
      if (makeThirdConv!=0):            # Если делаем третий свёрточный слой
      # Добавляем Conv2D-слой с thirdConvSize нейронами и ядром (thirdConvKernel)
        model.add(Conv2D(thirdConvSize, thirdConvKernel, activation=аctivation_list[thirdActivation0], padding=paddingType_list[thirdPaddingType0]))
      # делаем ли второй сверточный слой
      if makeThirdConv1!=0:
        model.add(Conv2D(thirdConvSize1, thirdConvKernel1, activation=аctivation_list[thirdActivation1], padding=paddingType_list[thirdPaddingType1]))
      # делаем ли третий сверточный слой
      if makeThirdConv2!=0:
        model.add(Conv2D(thirdConvSize2, thirdConvKernel2, activation=аctivation_list[thirdActivation2], padding=paddingType_list[thirdPaddingType2]))
      if (makeMaxPooling2!=0):        # Если делаем MaxPooling
      # Добавляем слой MaxPooling2D с размером (maxPoolingSize, maxPoolingSize)
        model.add(MaxPooling2D(pool_size=maxPoolingSize2)) 
      if (batchnorm2!=0):                 #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if (droppout2!=0):                 # Если добавляем Dropout в первый блок
        model.add(Dropout(dropout_list[dropout_size2]))   
      if flat_globMax_globAver==0:
        model.add(Flatten())                         # Добавляем слой Flatten
      elif flat_globMax_globAver==1:
        model.add(GlobalMaxPooling2D())              # Добавляем слой GlobalMaxPooling2D
      else:
        model.add(GlobalAveragePooling2D())          # Добавляем слой GlobalAveragePooling2D
    #['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge']  
    # если используем предобученные модели
    else:
      if (makeFirstNormalization!=0):   
        # Добавляем слой BatchNormalization
        model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels))) 
        # NASNetMobile
        if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
          nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))
          model.add(Resizing(224, 224, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_conv)
        # ResNet50
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
          resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet50_conv.layers:
            layer.trainable=False
          preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input
          model.add(Lambda(preprocess_input_resnet50, name='preprocessing'))
          model.add(resnet50_conv)
        # ResNet50V2
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
          resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet_v2_conv.layers:
            layer.trainable=False
          preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input
          model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing'))
          model.add(resnet_v2_conv)
        # VGG16
        elif pretrained_model_list[pretrained_model_name] == 'VGG16':
          vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg16_conv.layers:
            layer.trainable=False
          preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input
          model.add(Lambda(preprocess_input_vgg16, name='preprocessing'))
          model.add(vgg16_conv)
        # VGG19
        elif pretrained_model_list[pretrained_model_name] == 'VGG19':
          vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg19_conv.layers:
            layer.trainable=False
          preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input
          model.add(Lambda(preprocess_input_vgg19, name='preprocessing'))
          model.add(vgg19_conv)
        # Xception
        elif pretrained_model_list[pretrained_model_name] == 'Xception':
          xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in xception_conv.layers:
            layer.trainable=False
          preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input
          model.add(Lambda(preprocess_input_xception, name='preprocessing'))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(xception_conv)
        # EfficientNet
        elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
          efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in efficientnet_conv.layers:
            layer.trainable=False
          preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input
          model.add(Lambda(preprocess_input_efficientnet, name='preprocessing'))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(efficientnet_conv)
        # NASNetLarge
        elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
          nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_large_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))
          model.add(Resizing(331, 331, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_large_conv)
      # Если не делаем Batchnormalization
      else:
        if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
          nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(224, 224, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_conv)

        elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
          resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet50_conv.layers:
            layer.trainable=False
          preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input
          model.add(Lambda(preprocess_input_resnet50, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(resnet50_conv)
        # ResNet50V2
        elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
          resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in resnet_v2_conv.layers:
            layer.trainable=False
          preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input
          model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(resnet_v2_conv)
        # VGG16
        elif pretrained_model_list[pretrained_model_name] == 'VGG16':
          vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg16_conv.layers:
            layer.trainable=False
          preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input
          model.add(Lambda(preprocess_input_vgg16, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(vgg16_conv)
        # VGG19
        elif pretrained_model_list[pretrained_model_name] == 'VGG19':
          vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in vgg19_conv.layers:
            layer.trainable=False
          preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input
          model.add(Lambda(preprocess_input_vgg19, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(vgg19_conv)
        # Xception
        elif pretrained_model_list[pretrained_model_name] == 'Xception':
          xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in xception_conv.layers:
            layer.trainable=False
          preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input
          model.add(Lambda(preprocess_input_xception, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(xception_conv)
        # EfficientNet
        elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
          efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in efficientnet_conv.layers:
            layer.trainable=False
          preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input
          model.add(Lambda(preprocess_input_efficientnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(299, 299, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(efficientnet_conv)
        # NASNetLarge
        elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
          nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')
          for layer in nasnet_large_conv.layers:
            layer.trainable=False
          preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input
          model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))
          model.add(Resizing(331, 331, interpolation="bilinear", crop_to_aspect_ratio=False))
          model.add(nasnet_large_conv)

    
      model.add(Flatten())                         # Добавляем слой Flatten

    # Добавляем слой Dense с denseSize нейронами
    model.add(Dense(denseSize, activation=denseActivation_list[activation3]))
    if firstDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
      model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
    if firstDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
      model.add(Dropout(dropout_list[firstDenseDropoutSize]))

    if secondDense!=0:
      # Добавляем слой Dense с denseSize нейронами
      model.add(Dense(secondDenseSize, activation=denseActivation_list[secondDenseActivation]))
      if secondDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if secondDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
        model.add(Dropout(dropout_list[secondDenseDropoutSize]))


    if thirdDense!=0:
      # Добавляем слой Dense с denseSize нейронами
      model.add(Dense(thirdDenseSize, activation=denseActivation_list[thirdDenseActivation]))
      if thirdDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
        model.add(BatchNormalization())   # Добавляем слой BatchNormalization 
      if thirdDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
        model.add(Dropout(dropout_list[thirdDenseDropoutSize]))


    # Добавляем Dense-слой с softmax  или sigmoid-активацией и 3 нейронами
    model.add(Dense(CLASS_COUNT, activation=final_activation_list[final_activation])) 
    
    return model                      # Возвращаем модель
  def evaluateNet(net, ep, verb):
    # если используем не предобученную модель, то батчсайз =64
    if (net[81]==0):
      b_size=64
    # если используем предобученную модель, то батчсайз зависит от модели
    else:
      if pretrained_model_list[net[82]]=='NASNetMobile' or pretrained_model_list[net[82]]=='ResNet50' or pretrained_model_list[net[82]]=='ResNet50V2' or pretrained_model_list[net[82]]=='VGG16' or pretrained_model_list[net[82]]=='VGG19':
        b_size=64
      else:
        b_size=8
    if CLASS_COUNT==2:
      loss_func = 'binary_crossentropy'
    else:
      loss_func = 'categorical_crossentropy'
    val = 0
    time.time()
    model = createConvNet(net) # Создаем модель createConvNet
    opt_type = net[83]
    
    optimizer=optimizer_type_list[opt_type]

    # Компилируем сеть
    model.compile(loss=loss_func, optimizer=optimizer, metrics=['accuracy'])

    # Обучаем сеть на данных с фото водителей
    history = model.fit(x_train, 
                        y_train, 
                        batch_size=b_size, 
                        epochs=ep,
                        validation_split=0.1,
                        verbose=verb)
      
    val = history.history["val_accuracy"][-1] # Возвращаем точность на проверочной выборке с последней эпохи
    return val, model  


  
  nnew = n - nsurv    # Количество новых (столько новых ботов создается)
  l = 84              # Размер бота
  mut = 0.01          # Коэффициент мутаций
  popul = []          # Массив популяции
  val = []            # Одномерный массив значений точности этих ботов
  mean_val = []       # Массив со средними точностями по запускам
  max_val = []        # Массив с лучшими точностями по запускам
  best_models  =[]    # 3 лучших модели по итогам всех запусков
  worst_models = []   # 3 худших модели по итогам всех запусков

  from google.colab import drive
  import os.path
  from os import path
  import pandas as pd
  import ast

  drive.mount('/content/drive')
  base_filename = 'bots_accuracy_df.csv'

  df=pd.read_csv(os.path.join(link, base_filename))

  popul_col = df['bots'].tolist()
  new_bots_list = []
  for i in popul_col:
    new_bots_list.append(ast.literal_eval(i))

  accuracy_col = df['accuracy'].tolist()
  popul = new_bots_list
  best_bots_accuracy_list = accuracy_col

  sval = sorted(best_bots_accuracy_list, reverse=1)         # Сортируем best_bots_accuracy_list по убыванию точности

  # Получаем индексы ботов из списка по убыванию точности в данном запуске генетики sval:
  indexes_best = []
  for i in range(len(sval)):
    indexes_best.append(best_bots_accuracy_list.index(sval[i]))

  worst_val = sorted(best_bots_accuracy_list, reverse=0)    # Сортируем best_bots_accuracy_list по возрастанию точности
  current_mean_val = mean(best_bots_accuracy_list)          # Средняя точность ботов на каждом запуске по кол-ву запусков
  current_max_val = max(best_bots_accuracy_list)            # Лучшая из лучших точностей ботов на каждом запуске по кол-ву запусков
  mean_val.append(current_mean_val)
  max_val.append(current_max_val)

  newpopul = []                         # Создаем пустой список под новую популяцию
  for i in range(nsurv):                # Пробегаем по всем выжившим ботам
    index = best_bots_accuracy_list.index(sval[i])          # Получаем индекс очередного бота из списка лучших в списке val
    newpopul.append(popul[index])       # Добавляем в новую популяцию бота из popul с индексом index
      
  for i in range(nnew):                 # Проходимся в цикле nnew-раз  
    indexp1 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
    indexp2 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
    botp1 = newpopul[indexp1]           # Получаем первого бота-родителя по indexp1
    botp2 = newpopul[indexp2]           # Получаем второго бота-родителя по indexp2    
    newbot = []                         # Создаем пустой список под значения нового бота    
    net4Mut = createRandomNet()         # Создаем случайную сеть для мутаций
    for j in range(l):                  # Пробегаем по всей длине размерности (84)      
      x = 0      
      pindex = random.random()          # Получаем случайное число в диапазоне от 0 до 1

      # Если pindex меньше 0.5, то берем значения от первого бота, иначе от второго
      if pindex < 0.5:
        x = botp1[j]
      else:
        x = botp2[j]
        
        # С вероятностью mut устанавливаем значение бота из net4Mut
      if (random.random() < mut):
        x = net4Mut[j]
          
      newbot.append(x)                  # Добавляем очередное значение в нового бота      
    newpopul.append(newbot)             # Добавляем бота в новую популяцию      
  popul = newpopul                      # Записываем в popul новую посчитанную популяцию

  for it in range(epohs):                 # Пробегаем по всем запускам генетики
    #val = []                             # список с точностями ботов на проверочной выборке с последней эпохи
    curr_time = time.time()
    curr_models=[[] for _ in range(n)]    # список с моделями из данного запуска
    bots_accuracy_list = [[] for _ in range(n)] # создаем список с n пустыми списками под точности бота

    # для каждого бота создается список, в который будут добавляться точности на каждом запуске:
    
    for j in range(times_for_popul):
      for i in range(n):                    # Пробегаем в цикле по всем ботам 
        bot = popul[i]                      # Берем очередного бота
        f, model_sum = evaluateNet(bot, ep, verb) # Вычисляем точность текущего бота на последней эпохе и получаем обученную модель
        #val.append(f)                       # Добавляем полученное значение в список val
        bots_accuracy_list[i].append(f)
        curr_models[i].append(model_sum)       # Добавляем текущую модель в список с моделями curr_models
    best_bots_accuracy_list = []            # список из лучших точностей по каждому боту
    for acc in bots_accuracy_list:
      best_bots_accuracy_list.append(max(acc))

    #best_curr_models = []
    sval = sorted(best_bots_accuracy_list, reverse=1)         # Сортируем best_bots_accuracy_list по убыванию точности

    # Получаем индексы ботов из списка по убыванию точности в данном запуске генетики sval:
    indexes_best = []
    for i in range(len(sval)):
      indexes_best.append(best_bots_accuracy_list.index(sval[i]))

    # Получаем список моделей по ботам
    models_curr_list = []
    for i in curr_models:
      models_curr_list.append(i[0])

    # Получаем отсортированный список моделей по убыванию точности
    best_models = []
    for i in indexes_best:
      best_models.append(models_curr_list[i])

    ind_best = indexes_best[0]                                # Индекс лучшего бота в популяции
    ind_worst = indexes_best[-1]                              # Индекс худшего бота в популяции
    worst_val = sorted(best_bots_accuracy_list, reverse=0)    # Сортируем best_bots_accuracy_list по возрастанию точности
    
    current_mean_val = mean(best_bots_accuracy_list)          # Средняя точность ботов на каждом запуске по кол-ву запусков
    current_max_val = max(best_bots_accuracy_list)            # Лучшая из лучших точностей ботов на каждом запуске по кол-ву запусков
    mean_val.append(current_mean_val)
    max_val.append(current_max_val)
    # сохраняем текущую популяцию ботов и их лучшую аккураси по итогам всех запусков одной популяции на гугл драйв
    bots_accuracy_df = pd.DataFrame(
      {'bots': popul,
      'accuracy': best_bots_accuracy_list
      })
    base_filename = 'bots_accuracy_df.csv'
    os.path.join(link, base_filename)
    bots_accuracy_df.to_csv(os.path.join(link, base_filename), index=False)
    
    # Выводим точность 
    print("запуск номер ", (int(it)+1), " Секунд на запуск: ", int(time.time() - curr_time), " лучший бот - ", popul[ind_best]) 
    print(" Средняя точность ботов на последней эпохе ", current_mean_val,  "худший бот в данном запуске: ", popul[ind_worst])
    print(" Лучшая точность ботов на последней эпохе ", current_max_val)
    print("model_summary лучшей модели ", best_models[0].summary(), "model_summary худшей модели ", best_models[-1].summary()) 
    
    newpopul = []                         # Создаем пустой список под новую популяцию
    for i in range(nsurv):                # Пробегаем по всем выжившим ботам
      index = best_bots_accuracy_list.index(sval[i])          # Получаем индекс очередного бота из списка лучших в списке val
      newpopul.append(popul[index])       # Добавляем в новую популяцию бота из popul с индексом index
      
    for i in range(nnew):                 # Проходимся в цикле nnew-раз  
      indexp1 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
      indexp2 = random.randint(0,nsurv-1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
      botp1 = newpopul[indexp1]           # Получаем первого бота-родителя по indexp1
      botp2 = newpopul[indexp2]           # Получаем второго бота-родителя по indexp2    
      newbot = []                         # Создаем пустой список под значения нового бота    
      net4Mut = createRandomNet()         # Создаем случайную сеть для мутаций
      for j in range(l):                  # Пробегаем по всей длине размерности (84)      
        x = 0      
        pindex = random.random()          # Получаем случайное число в диапазоне от 0 до 1

        # Если pindex меньше 0.5, то берем значения от первого бота, иначе от второго
        if pindex < 0.5:
          x = botp1[j]
        else:
          x = botp2[j]
        
        # С вероятностью mut устанавливаем значение бота из net4Mut
        if (random.random() < mut):
          x = net4Mut[j]
          
        newbot.append(x)                  # Добавляем очередное значение в нового бота      
      newpopul.append(newbot)             # Добавляем бота в новую популяцию      
    popul = newpopul                      # Записываем в popul новую посчитанную популяцию

  final_best_models = []
  for i in range(best_models_num):        # Пробегаем по всем моделям из последнего запуска
    index = best_bots_accuracy_list.index(sval[i])            # Получаем индекс модели из списка лучших в списке best_bots_accuracy_list
    final_best_models.append(best_models[index])# Добавляем в best_models модель с индексом index

  for i in range(worst_models_num):        # Пробегаем по всем моделям из последнего запуска
    index = best_bots_accuracy_list.index(worst_val[i])        # Получаем индекс модели из списка худших в списке val
    worst_models.append(best_models[index])# Добавляем в worst_models модель с индексом index
    
  return best_models, worst_models, mean_val, max_val            # Функция возвращает 3 лучшие и 3 худшие модели, массив со средними и лучшими точностями по запускам



def best_bot_decoding(net, l_rate = 1e-5, activation_list = ['softmax','sigmoid','linear','relu','tanh'], 
                      paddingType_list = ["same", "same"], dropout_list = [0.05, 0.1, 0.3, 0.4, 0.5],
                      pretrained_model_list = ['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge'],
                       CLASS_COUNT=10):
  
  
  print("model = Sequential()")             
  
  makeFirstNormalization = net[0]  # Делаем ли нормализацию в начале
  firstConvSize = 2 ** net[1]      # Размер первого свёрточного слоя
  firstConvKernel = net[2]         # Ядро первого свёрточного слоя
  firstActivation0 = net[3]        # Функция активации первого слоя первого блока
  firstPaddingType0 = net[26]      # Какой padding используем для 1 слоя 1 блока - same или valid
  makeFirstConv1 = net[36]         # Делаем ли в первом блоке второй слой Conv2D
  firstConvSize1 = 2 ** net[42]    # Размер свертки второго Conv2D в первом блоке
  firstConvKernel1 = net[48]       # Ядро второго свёрточного слоя в первом блоке
  firstPaddingType1 = net[60]      # Тип паддинга для второго слоя первого блока
  firstActivation1 = net[54]       # Функция активации второго слоя первого блока
  makeFirstConv2 = net[37]         # Делаем ли в первом блоке третий слой Conv2D
  firstConvSize2 = 2 ** net[43]    # Размер свертки третьего Conv2D в первом блоке
  firstConvKernel2 = net[49]       # Ядро третьего свёрточного слоя в первом блоке
  firstPaddingType2 = net[61]      # Тип паддинга для третьего слоя первого блока
  firstActivation2 = net[55]       # Функция активации третьего слоя первого блока
  makeMaxPooling0 = net[4]         # Делаем ли maxpooling для первого блока
  maxPoolingSize0 = net[5]         # Размер MaxPooling
  droppout0 = net[22]              # Делаем ли Dropout в первом блоке
  dropout_size0 = net[23]          # Процент Dropout в первом блоке
  batchnorm0 = net[29]             # делаем ли нормализацию после первого блока
  firstActivation_list0 = ['softmax','sigmoid','linear','relu','tanh']   # какие функции активации тестируем в 1 сверточном блоке в 1 слое
  firstActivation_list1 = ['softmax','sigmoid','linear','relu','tanh']   # какие функции активации тестируем в 1 сверточном блоке во 2 слое
  firstActivation_list2 = ['softmax','sigmoid','linear','relu','tanh']   # какие функции активации тестируем в 1 сверточном блоке в 3 слое
  firstPaddingType_list0 = ["same", "valid"]                             # какие типы паддингов тестируем в 1 слое в 1 сверточном блоке
  firstPaddingType_list1 = ["same", "valid"]                             # какие типы паддингов тестируем во 2 слое в 1 сверточном блоке
  firstPaddingType_list2 = ["same", "valid"]                             # какие типы паддингов тестируем в 3 слое в 1 сверточном блоке
  makeSecondConv = net[6]          # Делаем ли второй свёрточный слой
  secondConvSize = 2 ** net[7]     # Размер второго свёрточного слоя
  secondConvKernel = net[8]        # Ядро второго свёрточного слоя
  secondPaddingType0 = net[34]     # Какой padding используем для 1 слоя 2 блока - same или valid
  secondActivation0 = net[11]      # Функция активации для первого слоя второго блока
  makeSecondConv1 = net[38]        # Делаем ли во втором блоке второй слой Conv2D
  secondConvSize1 = 2 ** net[44]   # Размер свертки второго Conv2D во втором блоке
  secondConvKernel1 = net[50]      # Ядро второго свёрточного слоя во втором блоке
  secondPaddingType1 = net[62]     # Тип паддинга для второго слоя второго блока
  secondActivation1 = net[56]      # Функция активации второго слоя второго блока
  makeSecondConv2 = net[39]        # Делаем ли во втором блоке третий слой Conv2D
  secondConvSize2 = 2 ** net[45]   # Размер свертки третьего Conv2D во втором блоке
  secondConvKernel2 = net[51]      # Ядро третьего свёрточного слоя во втором блоке
  secondPaddingType2 = net[63]     # Тип паддинга для третьего слоя второго блока
  secondActivation2 = net[57]      # Функция активации третьего слоя второго блока
  makeMaxPooling1 = net[9]         # Делаем ли MaxPooling во втором блоке
  maxPoolingSize1 = net[10]        # Размер MaxPooling во втором блоке
  droppout1 = net[27]              # Dropout во втором блоке
  dropout_size1 = net[32]          # Процент Dropout во втором блоке
  batchnorm1 = net[30]             # делаем ли нормализацию после второго блока
  secondActivation_list0 = ['softmax','sigmoid','linear','relu','tanh']  # какие функции активации тестируем во 2 сверточном блоке в 1 слое
  secondActivation_list1 = ['softmax','sigmoid','linear','relu','tanh']  # какие функции активации тестируем во 2 сверточном блоке во 2 слое
  secondActivation_list2 = ['softmax','sigmoid','linear','relu','tanh']  # какие функции активации тестируем во 2 сверточном блоке в 3 слое
  secondPaddingType_list0 = ["same", "valid"]                            # какие типы паддингов тестируем в 1 слое во 2 сверточном блоке
  secondPaddingType_list1 = ["same", "valid"]                            # какие типы паддингов тестируем во 2 слое во 2 сверточном блоке
  secondPaddingType_list2 = ["same", "valid"]                            # какие типы паддингов тестируем в 3 слое во 2 сверточном блоке
  makeThirdConv = net[12]          # Делаем ли третий свёрточный слой
  thirdConvSize = 2 ** net[13]     # Размер третьего свёрточного слоя
  thirdConvKernel = net[14]        # Ядро третьего свёрточного слоя
  thirdPaddingType0 = net[35]      # Какой padding используем для 1 слоя 3 блока - same или valid
  thirdActivation0 = net[17]       # Функция активации для первого слоя третьего блока
  makeThirdConv1 = net[40]         # Делаем ли в третьем блоке второй слой Conv2D
  thirdConvSize1 = 2 ** net[46]    # Размер свертки второго Conv2D в третьем блоке
  thirdConvKernel1 = net[52]       # Ядро второго свёрточного слоя в третьем блоке
  thirdPaddingType1 = net[64]      # Тип паддинга для второго слоя третьего блока
  thirdActivation1 = net[58]       # Функция активации второго слоя третьего блока
  makeThirdConv2 = net[41]         # Делаем ли в третьем блоке третий слой Conv2D
  thirdConvSize2 = 2 ** net[47]    # Размер свертки третьего Conv2D в третьем блоке
  thirdConvKernel2 = net[53]       # Ядро третьего свёрточного слоя в третьем блоке
  thirdPaddingType2 = net[65]      # Тип паддинга для третьего слоя третьего блока
  thirdActivation2 = net[59]       # Функция активации третьего слоя третьего блока
  makeMaxPooling2 = net[15]        # Делаем ли MaxPooling в третьем блоке
  maxPoolingSize2 = net[16]        # Размер MaxPooling в третьем блоке
  droppout2 = net[28]              # Делаем ли Dropout в третьем блоке
  dropout_size2 = net[33]          # Процент Dropout в третьем блоке
  batchnorm2 = net[31]             # делаем ли нормализацию после третьего блока
  thirdActivation_list0 = ['softmax','sigmoid','linear','relu','tanh']    # какие функции активации тестируем в 3 сверточном блоке в 1 слое
  thirdActivation_list1 = ['softmax','sigmoid','linear','relu','tanh']    # какие функции активации тестируем в 3 сверточном блоке во 2 слое
  thirdActivation_list2 = ['softmax','sigmoid','linear','relu','tanh']    # какие функции активации тестируем в 3 сверточном блоке в 3 слое
  thirdPaddingType_list0 = ["same", "same"]                               # какие типы паддингов тестируем в 1 слое в 3 сверточном блоке
  thirdPaddingType_list1 = ["same", "same"]                               # какие типы паддингов тестируем во 2 слое в 3 сверточном блоке
  thirdPaddingType_list2 = ["same", "same"]                               # какие типы паддингов тестируем в 3 слое в 3 сверточном блоке
  activation3 = net[18]                                                   # Функция активации для предпоследнего dense слоя
  activation4 = net[19]                                                   # Функция активации для последнего слоя
  flat_globMax_globAver = net[20]                                         # тестируем Flatten, GlobalMaxPooling2D или GlobalAveragePooling2D
  denseSize = 2 ** net[21]                                                # Размер первого полносвязного слоя
  secondDense = net[66]                                                   # Создание второго полносвязного слоя
  thirdDense = net[67]                                                    # Создание третьего полносвязного слоя
  secondDenseSize = 2 ** net[68]                                          # Размер второго полносвязного слоя
  thirdDenseSize = 2 ** net[69]                                           # Размер третьего полносвязного слоя
  secondDenseActivation_list = ['softmax','sigmoid','linear','relu','tanh'] # какие функции активации тестируем во втором полносвязном слое (список)
  thirdDenseActivation_list = ['softmax','sigmoid','linear','relu','tanh']  # какие функции активации тестируем в третьем полносвязном слое (список)
  secondDenseActivation = net[70]                                           # какие функции активации тестируем во втором полносвязном слое
  thirdDenseActivation = net[71]                                            # какие функции активации тестируем в третьем полносвязном слое
  firstDenseBatchnorm = net[72]                                             # делаем ли нормализацию после первого полносвязного слоя
  secondDenseBatchnorm = net[73]                                            # делаем ли нормализацию после второго полносвязного слоя
  thirdDenseBatchnorm = net[74]                                             # делаем ли нормализацию после третьего полносвязного слоя
  firstDenseDropout = net[75]                                               # делаем ли Dropout после первого полносвязного слоя
  secondDenseDropout = net[76]                                              # делаем ли Dropout после второго полносвязного слоя
  thirdDenseDropout = net[77]                                               # делаем ли Dropout после третьего полносвязного слоя
  firstDenseDropoutSize = net[78]                                           # процент Dropout после первого полносвязного слоя
  secondDenseDropoutSize = net[79]                                          # процент Dropout после второго полносвязного слоя
  thirdDenseDropoutSize = net[80]                                           # процент Dropout после третьего полносвязного слоя
  test_activations = net[24]       # Тестируем ли функции активации - в моменте не используется
  final_activation = net[25]       # Какие активации тестируем на последнем слое - sigmoid или softmax
  final_activation_list = ['softmax','sigmoid']                     # какие функции активации тестируем в последнем полносвязном слое
  dropout_list = [0.05, 0.1, 0.3, 0.4, 0.5]
  activation_list3 = ['softmax','sigmoid','linear','relu','tanh']   # какие функции активации тестируем в предпоследнем полносвязном слое
  use_pretrained_model = net[81]                                            # Используем ли предобученные модели
  pretrained_model_name = net[82]                                           # Название предобученной модели
  optimizer_type = net[83]                                                  # Какой optimizer применяем
  optimizer_type_list = ['SGD', 'RMSprop', 'Adam', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl']
  if (use_pretrained_model==0):

    if (makeFirstNormalization!=0):   
      print("model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))") 
      print(f"model.add(Conv2D({firstConvSize}, {firstConvKernel}, activation='{firstActivation_list0[firstActivation0]}, padding='{firstPaddingType_list0[firstPaddingType0]}'))")
    else:
      print(f"model.add(Conv2D({firstConvSize}, {firstConvKernel}, input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels), activation='{firstActivation_list0[firstActivation0]}', padding='{firstPaddingType_list0[firstPaddingType0]}'))")
    if makeFirstConv1!=0:
      print(f"model.add(Conv2D({firstConvSize1}, {firstConvKernel1}, activation='{firstActivation_list1[firstActivation1]}', padding='{firstPaddingType_list1[firstPaddingType1]}'))")
    # делаем ли третий сверточный слой
    if makeFirstConv2!=0:
      print(f"model.add(Conv2D({firstConvSize2}, {firstConvKernel2}, activation='{firstActivation_list2[firstActivation2]}', padding='{firstPaddingType_list2[firstPaddingType2]}'))")
    if makeMaxPooling0!=0:            # Если делаем maxpooling
      print(f"model.add(MaxPooling2D({maxPoolingSize0}))")
    if (batchnorm0!=0):                 #  если добавляем слой BatchNormalization
      print("model.add(BatchNormalization())") # Добавляем слой BatchNormalization 
    if (droppout0!=0):                 # Если добавляем Dropout в первый блок
      print(f"model.add(Dropout({dropout_list[dropout_size0]}))")         
    if (makeSecondConv!=0):           # Если делаем второй свёрточный слой
      print(f"model.add(Conv2D({secondConvSize}, {secondConvKernel}, activation='{secondActivation_list0[secondActivation0]}, padding={secondPaddingType_list0[secondPaddingType0]}'))")  
    if makeSecondConv1!=0:
      print(f"model.add(Conv2D({secondConvSize1}, {secondConvKernel1}, activation= '{secondActivation_list1[secondActivation1]}, padding={secondPaddingType_list1[secondPaddingType1]}'))")
    if makeSecondConv2!=0:
      print(f"model.add(Conv2D({secondConvSize2}, {secondConvKernel2} activation='{secondActivation_list2[secondActivation2]}, padding='{secondPaddingType_list2[secondPaddingType2]}'))")
  
    if (makeMaxPooling1!=0):        # Если делаем MaxPooling
    # Добавляем слой MaxPooling2D с размером (maxPoolingSize)
      print(f"model.add(MaxPooling2D(pool_size={maxPoolingSize1}))") 
    if (batchnorm1!=0):                
      print("model.add(BatchNormalization())")   
    if (droppout1!=0):                 
      print(f"model.add(Dropout({dropout_list[dropout_size1]}'))")   
    if (makeThirdConv!=0):            
      print(f"model.add(Conv2D({thirdConvSize} ,{thirdConvKernel} , activation='{thirdActivation_list0[thirdActivation0]}, padding='{thirdPaddingType_list0[thirdPaddingType0]}'))")
    if makeThirdConv1!=0:
      print(f"model.add(Conv2D({thirdConvSize1}, {thirdConvKernel1}, activation='{thirdActivation_list1[thirdActivation1]}', padding='{thirdPaddingType_list1[thirdPaddingType1]}'))")
    if makeThirdConv2!=0:
      print(f"model.add(Conv2D({thirdConvSize2},{thirdConvKernel2} activation='{thirdActivation_list2[thirdActivation2]}', padding='{thirdPaddingType_list2[thirdPaddingType2]}'))")
    if (makeMaxPooling2!=0):        
      print(f"model.add(MaxPooling2D(pool_size={maxPoolingSize2}))") 
    if (batchnorm2!=0):                 #  если добавляем слой BatchNormalization
      print("model.add(BatchNormalization())")   # Добавляем слой BatchNormalization 
    if (droppout2!=0):                 # Если добавляем Dropout в первый блок
      print(f"model.add(Dropout({dropout_list[dropout_size2]}))")   
    if flat_globMax_globAver==0:
      print("model.add(Flatten())")                         # Добавляем слой Flatten
    elif flat_globMax_globAver==1:
      print("model.add(GlobalMaxPooling2D())")              # Добавляем слой GlobalMaxPooling2D
    else:
      print("model.add(GlobalAveragePooling2D())")          # Добавляем слой GlobalAveragePooling2D
    
  # если используем предобученные модели
  else:
    if (makeFirstNormalization!=0):   
      # Добавляем слой BatchNormalization
      print("model.add(BatchNormalization(input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))") 
      # NASNetMobile
      if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
        print("nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in nasnet_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))")
        print("model.add(Resizing(224, 224, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(nasnet_conv)")
      # ResNet50
      elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
        print("resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in resnet50_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input")
        print("model.add(Lambda(preprocess_input_resnet50, name='preprocessing'))")
        print("model.add(resnet50_conv)")
      # ResNet50V2
      elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
        print("resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in resnet_v2_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input")
        print("model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing'))")
        print("model.add(resnet_v2_conv)")
      # VGG16
      elif pretrained_model_list[pretrained_model_name] == 'VGG16':
        print("vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in vgg16_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input")
        print("model.add(Lambda(preprocess_input_vgg16, name='preprocessing'))")
        print("model.add(vgg16_conv)")
      # VGG19
      elif pretrained_model_list[pretrained_model_name] == 'VGG19':
        print("vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in vgg19_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input")
        print("model.add(Lambda(preprocess_input_vgg19, name='preprocessing'))")
        print("model.add(vgg19_conv)")
      # Xception
      elif pretrained_model_list[pretrained_model_name] == 'Xception':
        print("xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in xception_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input")
        print("model.add(Lambda(preprocess_input_xception, name='preprocessing'))")
        print("model.add(Resizing(299, 299, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(xception_conv)")
      # EfficientNet
      elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
        print("efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in efficientnet_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_efficientnet, name='preprocessing'))")
        print("model.add(Resizing(299, 299, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(efficientnet_conv)")
      # NASNetLarge
      elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
        print("nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in nasnet_large_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_nasnet, name='preprocessing'))")
        print("model.add(Resizing(331, 331, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(nasnet_large_conv)")
    # Если не делаем Batchnormalization
    else:
      if pretrained_model_list[pretrained_model_name] == 'NASNetMobile':
        print("nasnet_conv = tensorflow.keras.applications.nasnet.NASNetMobile(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in nasnet_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(Resizing(224, 224, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(nasnet_conv)")

      elif pretrained_model_list[pretrained_model_name] == 'ResNet50':
        print("resnet50_conv = tensorflow.keras.applications.resnet50.ResNet50(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in resnet50_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_resnet50 = tensorflow.keras.applications.resnet50.preprocess_input")
        print("model.add(Lambda(preprocess_input_resnet50, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(resnet50_conv)")
      # ResNet50V2
      elif pretrained_model_list[pretrained_model_name] == 'ResNet50V2':
        print("resnet_v2_conv = tensorflow.keras.applications.resnet_v2.ResNet50V2(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in resnet_v2_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_resnet_v2 = tensorflow.keras.applications.resnet_v2.preprocess_input")
        print("model.add(Lambda(preprocess_input_resnet_v2, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(resnet_v2_conv)")
      # VGG16
      elif pretrained_model_list[pretrained_model_name] == 'VGG16':
        print("vgg16_conv = tensorflow.keras.applications.vgg16.VGG16(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in vgg16_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_vgg16 = tensorflow.keras.applications.vgg16.preprocess_input")
        print("model.add(Lambda(preprocess_input_vgg16, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(vgg16_conv)")
      # VGG19
      elif pretrained_model_list[pretrained_model_name] == 'VGG19':
        print("vgg19_conv = tensorflow.keras.applications.vgg19.VGG19(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in vgg19_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_vgg19 = tensorflow.keras.applications.vgg19.preprocess_input")
        print("model.add(Lambda(preprocess_input_vgg19, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(vgg19_conv)")
      # Xception
      elif pretrained_model_list[pretrained_model_name] == 'Xception':
        print("xception_conv = tensorflow.keras.applications.xception.Xception(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in xception_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_xception = tensorflow.keras.applications.xception.preprocess_input")
        print("model.add(Lambda(preprocess_input_xception, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(Resizing(299, 299, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(xception_conv)")
      # EfficientNet
      elif pretrained_model_list[pretrained_model_name] == 'EfficientNet':
        print("efficientnet_conv = tensorflow.keras.applications.efficientnet.EfficientNetB7(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in efficientnet_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_efficientnet = tensorflow.keras.applications.efficientnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_efficientnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(Resizing(299, 299, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(efficientnet_conv)")
      # NASNetLarge
      elif pretrained_model_list[pretrained_model_name] == 'NASNetLarge':
        print("nasnet_large_conv = tensorflow.keras.applications.nasnet.NASNetLarge(include_top=False, pooling='avg', classes=CLASS_COUNT, weights='imagenet')")
        print("for layer in nasnet_large_conv.layers:")
        print("  layer.trainable=False")
        print("preprocess_input_nasnet = tensorflow.keras.applications.nasnet.preprocess_input")
        print("model.add(Lambda(preprocess_input_nasnet, name='preprocessing', input_shape=(IMG_WIDTH, IMG_HEIGHT, num_channels)))")
        print("model.add(Resizing(331, 331, interpolation='bilinear', crop_to_aspect_ratio=False))")
        print("model.add(nasnet_large_conv)")

  
    print("model.add(Flatten())")

  # Добавляем слой Dense с denseSize нейронами
  print(f"model.add(Dense({denseSize}, activation='{activation_list3[activation3]}'))")
  if firstDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
    print("model.add(BatchNormalization())")   # Добавляем слой BatchNormalization 
  if firstDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
    print(f"model.add(Dropout({dropout_list[firstDenseDropoutSize]}))")

  if secondDense!=0:
    # Добавляем слой Dense с denseSize нейронами
    print(f"model.add(Dense({secondDenseSize}, activation='{secondDenseActivation_list[secondDenseActivation]}'))")
    if secondDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
      print("model.add(BatchNormalization())")   # Добавляем слой BatchNormalization 
    if secondDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
      print(f"model.add(Dropout({dropout_list[secondDenseDropoutSize]}))")


  if thirdDense!=0:
    # Добавляем слой Dense с denseSize нейронами
    print(f"model.add(Dense({thirdDenseSize} activation='{thirdDenseActivation_list[thirdDenseActivation]}'))")
    if thirdDenseBatchnorm!=0:           #  если добавляем слой BatchNormalization
      print(f"model.add(BatchNormalization())")   # Добавляем слой BatchNormalization 
    if thirdDenseDropout!=0:            # Если добавляем Dropout в первый полносвязный
      print(f"model.add(Dropout({dropout_list[thirdDenseDropoutSize]}))")


  # Добавляем Dense-слой с softmax  или sigmoid-активацией и CLASS_COUNT нейронами
  print(f"model.add(Dense(CLASS_COUNT, activation='{final_activation_list[final_activation]}'))")
  if CLASS_COUNT == 2:
    print(f"model.compile(loss=tf.keras.losses.BinaryCrossentropy, optimizer=tf.keras.optimizers.{optimizer_type_list[optimizer_type]}(learning_rate={l_rate}), metrics=['accuracy'])")
  else:
    print(f"model.compile(loss=tf.keras.losses.CategoricalCrossentropy, optimizer=tf.keras.optimizers.{optimizer_type_list[optimizer_type]}(learning_rate={l_rate}), metrics=['accuracy'])")





def show_info():
  module = input('Введите название модуля: IMG_create_Conv_Net, visualize_mean_accuracy, best_bot_decoding, Recovery_Conv_Net')
  if module == "IMG_create_Conv_Net":
    print("""IMG_create_Conv_Net - создает набор ботов (в количестве n), каждого бота обучает на определенном количестве эпох (параметр 'ep')
Созданный набор ботов обучается определенное количество раз (параметр "times_for_popul")
Далее по параметру accuracy (выбирается лучший показатель каждого бота) отбираются боты с самой высокой точностью в количестве, указанном в параметре "nsurv"
Популяция дополняется новыми ботами до изначального количества  (параметр "n") на основании лучших ботов с учетом коэффициента мутации.
Это и есть один цикл генетики. Таких циклов проводится определенное количество, указанное в параметре "epohs".
Обязательными параметрами функции являются обучающая и проверочная выборки: x_train y_train x_val y_val""")
    
    print("""Параметры:

1. Создание сверточной сети:
IMG_WIDTH = 64                          # Размеры изображения (ширина)
IMG_HEIGHT = 64                         # Размеры изображения (высота)
num_channels = 3                        # Количество каналов
CLASS_COUNT = 10                        # Количество классов (категорий)
pretrained_yes_no = 1                   # Применяем ли предобученные модели: 1=Да, 0= Нет
pretrained_model_list = [NASNetMobile, ResNet50, ResNet50V2, VGG16, VGG19, Xception, EfficientNet, NASNetLarge]   # В этом списке указываются предобученные модели,
                                        # которые алгоритм будет использовать при создании ботов. Он должен соответствовать параметру pretrained_model_type-1
pretrained_model_type = 7               # количество тестируемых предобученных моделей 
max_conv2D_units = 9                    # максимальное количество нейронов в сверточных слоях (минимум 4). Рассчитывается при помощи степени цифры 2. То есть, если указать 
                                        # "9", то максимальное значение нейронов в сверточных слоях будет 2**9=512
max_conv2D_kernel = 5                   # Максимальное значение ядра свёрточных слоях (Минимум 2)
second_Conv2D_block = 1                 # Делаем ли второй сверточный блок
third_Conv2D_block = 1                  # Делаем ли третий сверточный блок
if_maxpooling = 1                       # Делаем ли MaxPooling 
max_Maxpooling_size = 3                 # Максимальный размер MaxPooling (минимум 2)
activation_func = 4                     # Количество используемых функций активации в сверточных слоях (должна соответствовать параметру activation_func-1)
аctivation_list = ['softmax','sigmoid','linear','relu','tanh'] # Функции активации, используемые в сверточных слоях
padding_type = 1                        # Тип padding - same или valid - в первом сверточном блоке (должен соответствовать длине списка paddingType_list-1)
paddingType_list = ["same", "same"]    # какие типы паддингов тестируем в сверточных блоках
if_dropout = 1                          # Делаем ли dropout в сверточных блоках 
flatten_globalMax_globalAveragePool = 2 # тестируем ли Flatten, GlobalMax и GlobalAveragePooling
# 0 - тестируем только Flatten, 1-тестируем Flatten и GlobalMax, 2 - тестируем Flatten, GlobalMax и GlobalAveragePooling
if_batchnorm = 1                        # Делаем ли Batchnormalization 
second_dense =  1                       # Делаем ли второй полносвязный слой
third_dense = 1                         # Делаем ли третий полносвязный слой
dense_size = 7                          # Максимальный размер полносвязного слоя (минимум 4)Рассчитывается при помощи степени цифры 2. То есть, если указать 
                                        # "9", то максимальное значение нейронов в сверточных слоях будет 2**9=512
dense_activation = 4                    # Максимальное количество тестируемых функций активации полносвязного слоя (должно соответствовать параметру denseActivation_list-1)
denseActivation_list = ['softmax','sigmoid','linear','relu','tanh'] # какие функции активации тестируем в полносвязных слоях 
optimizer_type = 7                      # Какой тип оптимизатора используем (должно соответствовать параметру optimizer_type_list)
optimizer_type_list = ['SGD', 'RMSprop', 'Adam', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl'] # Список оптимизаторов
dense_batchnorm = 1                     # Делаем ли нормализацию после dense слоев
dense_dropout = 1                       # Делаем ли Dropout после dense слоев

2. Вычисление результата работы сети:
x_train 
y_train
x_val
y_val
ep = 10                                 # количество эпох, на которых будет обучаться каждый бот
verb = 1                                # Verbose - визуализация процесса обучения - 1 - визуализировать, 0 - без визуализации


3. Параметры генетики:
n = 20                                  # Общее число ботов
nsurv = 10                              # Количество выживших (столько лучших переходит в новую популяцию)
epohs = 5                               # Количество запусков генетики
times_for_popul = 5                     # Количество запусков одной популяции
best_models_num = 3                     # Сколько лучших моделей мы хотим получить по итогам всех запусков


Функция возвращает: 
mean_val, max_val, final_best_models, final_best_bot  # Получаем среднее и максимальное значение аккураси на проверочной выборке, 
                                                      # набор из final_best_models - количество лучших моделей, лучший бот на последнем запуске
    """)
  if module == "visualize_mean_accuracy":
    print("""Модуль visualize_mean_accuracy возвращает график обучения - среднюю и лучшую точности на каждом запуске генетики
Параметры:
mean_val - массив со средней точностью по каждому запуску генетики
max_val - массив с наилучшей точностью среди ботов на последней эпохе обучения по каждому запуску генетики""")
  if module == "best_bot_decoding":
    print("""Модуль best_bot_decoding расшифровывает лучшего бота на последнем запуске генетики (самая высокая точность на последней эпохе обучения)
Возвращает готовую структуру модели, соответствующую лучшему боту
Параметры по умолчанию:
net - лучший бот, которого расшифровываем
l_rate = learning_rate = 1e-5
Следующие списки должны совпадать с соответствующими списками,  указанными в модулях IMG_create_Conv_Net и Recovery_Conv_Net
activation_list = ['softmax','sigmoid','linear','relu','tanh']  # функции активации 
paddingType_list = ["same", "same"]
dropout_list = [0.05, 0.1, 0.3, 0.4, 0.5]
pretrained_model_list = ['NASNetMobile', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 'EfficientNet', 'NASNetLarge']
""")
  if module == "Recovery_Conv_Net":
    print("""Модуль Recovery_Conv_Net восстанавливает прерванное обучение на основании данных, сохраненных на гугл диск.
Параметры должны совпадать теми, что указывались при инициализации модуля  IMG_create_Conv_Net, за исключением переменной epohs,
которую следует устанавливать, учитывая уже проведенное количество запусков генетики.

Параметры по умолчанию
1. Создание сверточной сети:
IMG_WIDTH = 64                          # Размеры изображения (ширина)
IMG_HEIGHT = 64                         # Размеры изображения (высота)
num_channels = 3                        # Количество каналов
CLASS_COUNT = 10                        # Количество классов (категорий)
pretrained_yes_no = 1                   # Применяем ли предобученные модели: 1=Да, 0= Нет
pretrained_model_list = [NASNetMobile, ResNet50, ResNet50V2, VGG16, VGG19, Xception, EfficientNet, NASNetLarge]   # В этом списке указываются предобученные модели,
                                        # которые алгоритм будет использовать при создании ботов. Его длина должна соответствовать параметру pretrained_model_type
pretrained_model_type = 7               # количество тестируемых предобученных моделей 
max_conv2D_units = 9                    # максимальное количество нейронов в сверточных слоях (минимум 4). Рассчитывается при помощи степени цифры 2. То есть, если указать 
                                        # "9", то максимальное значение нейронов в сверточных слоях будет 2**9=512
max_conv2D_kernel = 5                   # Максимальное значение ядра свёрточных слоях (Минимум 2)
second_Conv2D_block = 1                 # Делаем ли второй сверточный блок
third_Conv2D_block = 1                  # Делаем ли третий сверточный блок
if_maxpooling = 1                       # Делаем ли MaxPooling 
max_Maxpooling_size = 3                 # Максимальный размер MaxPooling (минимум 2)
activation_func = 4                     # Количество используемых функций активации в сверточных слоях (должна соответствовать параметру activation_func)
аctivation_list = ['softmax','sigmoid','linear','relu','tanh'] # Функции активации, используемые в сверточных слоях
padding_type = 1                        # Тип padding - same или valid - в первом сверточном блоке (должен соответствовать длине списка paddingType_list)
paddingType_list = ["same", "same"]    # какие типы паддингов тестируем в сверточных блоках
if_dropout = 1                          # Делаем ли dropout в сверточных блоках 
flatten_globalMax_globalAveragePool = 2 # тестируем ли Flatten, GlobalMax и GlobalAveragePooling
# 0 - тестируем только Flatten, 1-тестируем Flatten и GlobalMax, 2 - тестируем Flatten, GlobalMax и GlobalAveragePooling
if_batchnorm = 1                        # Делаем ли Batchnormalization 
second_dense =  1                       # Делаем ли второй полносвязный слой
third_dense = 1                         # Делаем ли третий полносвязный слой
dense_size = 7                          # Максимальный размер полносвязного слоя (минимум 4)Рассчитывается при помощи степени цифры 2. То есть, если указать 
                                        # "9", то максимальное значение нейронов в сверточных слоях будет 2**9=512
dense_activation = 4                    # Максимальное количество тестируемых функций активации полносвязного слоя (должно соответствовать параметру denseActivation_list)
denseActivation_list = ['softmax','sigmoid','linear','relu','tanh'] # какие функции активации тестируем в полносвязных слоях 
optimizer_type = 7                      # Какой тип оптимизатора используем (должно соответствовать параметру optimizer_type_list)
optimizer_type_list = ['SGD', 'RMSprop', 'Adam', 'Adadelta', 'Adagrad', 'Adamax', 'Nadam', 'Ftrl'] # Список оптимизаторов
dense_batchnorm = 1                     # Делаем ли нормализацию после dense слоев
dense_dropout = 1                       # Делаем ли Dropout после dense слоев
2. Вычисление результата работы сети:
x_train 
y_train
x_val
y_val
ep = 10                                 # количество эпох, на которых будет обучаться каждый бот
verb = 1                                # Verbose - визуализация процесса обучения - 1 - визуализировать, 0 - без визуализации
3. Параметры генетики:
n = 20                                  # Общее число ботов
nsurv = 10                              # Количество выживших (столько лучших переходит в новую популяцию)
epohs = 5                               # Количество запусков генетики
times_for_popul = 5                     # Количество запусков одной популяции
best_models_num = 3                     # Сколько лучших моделей мы хотим получить по итогам всех запусков

Функция возвращает: 
mean_val, max_val, final_best_models, final_best_bot  # Получаем среднее и максимальное значение аккураси на проверочной выборке, 
                                                      # набор из final_best_models - количество лучших моделей, лучший бот на последнем запуске
""")