import numpy as np
import random
import os
import pickle

def create_data():
    buckets = pickle.load(open('static/pickles/buckets.pkl','rb'))
    images = pickle.load(open('static/pickles/images.pkl','rb'))
    audios = pickle.load(open('static/pickles/audios.pkl','rb'))
    
    #train = pickle.load(open('train_local.pkl','rb'))
    img2lab = pickle.load(open('static/pickles/img2lab.pkl','rb'))
    #print(train)
    
    for i in images:
        images[i] = ['static/images/'+j.split('/')[-1] for j in images[i]]
    for i in audios:
        audios[i] = ['static/audios/{}/{}'.format(j.split('/')[-2],j.split('/')[-1]) for j in audios[i]]
    
    train2 = []
    
    tempimg0 = []
    tempaud0 = []
    tempimg3 = []
    tempaud3 = []
    
    n = 3
    
    buckets = random.sample(buckets,6)
    for i in range(6):
        buckets[i] = random.sample(buckets[i],10)
    
    for x,k in enumerate([1,2,3]):
        temp = []
        for j in range(k):
            for i in buckets[x][:n]:
                a = random.sample(images[i],1)[0]
                del images[i][images[i].index(a)]
                b = random.sample(audios[img2lab[i]],1)[0]
                del audios[img2lab[i]][audios[img2lab[i]].index(b)]
                temp.append((a,b))
                if x==0:
                    tempimg0.append([a])
                    tempaud0.append([b])
                if x==3:
                    tempimg3.append([a])
                    tempaud3.append([b])
        train2.append(temp)
    
    imgtest = []
    audtest = []
    for z,bucket in enumerate(buckets[:3]):
        tempimg = []
        tempaud = []
        for i in bucket[:n]:
            a = random.sample(images[i],1)[0]
            del images[i][images[i].index(a)]
            b = random.sample(audios[img2lab[i]],1)[0]
            del audios[img2lab[i]][audios[img2lab[i]].index(b)]
            tempimg.append([a,b])
            
            a = random.sample(images[i],1)[0]
            del images[i][images[i].index(a)]
            b = random.sample(audios[img2lab[i]],1)[0]
            del audios[img2lab[i]][audios[img2lab[i]].index(b)]
            tempaud.append([b,a])
        
        for x,i in enumerate(bucket[:n]):
            for y,j in enumerate(random.sample(bucket[:x]+bucket[x+1:n],n-1)):
                b = random.sample(audios[img2lab[j]],1)[0]
    #            del audios[img2lab[j]][audios[img2lab[j]].index(b)]
                tempimg[x].append(b)
            
            for y,j in enumerate(random.sample(bucket[:x]+bucket[x+1:n],n-1)):
                a = random.sample(images[j],1)[0]
    #            del images[j][images[j].index(a)]
                tempaud[x].append(a)
            
            tempimg[x][1:] = random.sample(tempimg[x][1:],len(tempimg[x][1:]))
            tempaud[x][1:] = random.sample(tempaud[x][1:],len(tempaud[x][1:]))
        
    #    if z==0:
    #        for x,i in enumerate(bucket):
    #            for y,j in enumerate(random.sample(bucket[:x]+bucket[x:],10)):
    #                b = random.sample(audios[img2lab[j]],1)[0]
    #    #            del audios[img2lab[j]][audios[img2lab[j]].index(b)]
    #                tempimg0[x].append(b)
    #            
    #            for y,j in enumerate(random.sample(bucket[:x]+bucket[x:],10)):
    #                a = random.sample(images[j],1)[0]
    #    #            del images[j][images[j].index(a)]
    #                tempaud0[x].append(a)
    #            
    #            tempimg0[x][1:] = random.sample(tempimg[x][1:],len(tempimg0[x][1:]))
    #            tempaud0[x][1:] = random.sample(tempaud[x][1:],len(tempaud0[x][1:]))
    #            
    #        tempimg += tempimg0
    #        tempaud += tempaud0
    #    
    #    if z==3:
    #        for x,i in enumerate(bucket):
    #            for y,j in enumerate(random.sample(bucket[:x]+bucket[x:],10)):
    #                b = random.sample(audios[img2lab[j]],1)[0]
    #    #            del audios[img2lab[j]][audios[img2lab[j]].index(b)]
    #                tempimg3[x].append(b)
    #            
    #            for y,j in enumerate(random.sample(bucket[:x]+bucket[x:],10)):
    #                a = random.sample(images[j],1)[0]
    #    #            del images[j][images[j].index(a)]
    #                tempaud3[x].append(a)
    #            
    #            tempimg3[x][1:] = random.sample(tempimg[x][1:],len(tempimg3[x][1:]))
    #            tempaud3[x][1:] = random.sample(tempaud[x][1:],len(tempaud3[x][1:]))
    #        tempimg += tempimg3
    #        tempaud += tempaud3
        
        imgtest.append([tuple(i) for i in tempimg])
        audtest.append([tuple(i) for i in tempaud])
    
    train3 = []
    for j in range(3):
        train3.extend([i for i in train2[j]])
    
    imgtest3 = []
    audtest3 = []
    
    for i in [[0,1,2],[1,2,0],[2,0,1]]:
        for j in range(n):
            imgtest3.append(tuple([imgtest[i[0]][j][0]]+random.sample(list(imgtest[i[0]][j][1:])+list(imgtest[i[1]][random.randint(0,n-1)][1:])+list(imgtest[i[2]][random.randint(0,n-1)][1:]),3*n)))
            audtest3.append(tuple([audtest[i[0]][j][0]]+random.sample(list(audtest[i[0]][j][1:])+list(audtest[i[1]][random.randint(0,n-1)][1:])+list(audtest[i[2]][random.randint(0,n-1)][1:]),3*n)))
    
    with open('static/pickles/imgtest_demo.pkl','wb+') as fp:
        pickle.dump([imgtest3],fp)
    
    with open('static/pickles/audtest_demo.pkl','wb+') as fp:
        pickle.dump([audtest3],fp)
    
    with open('static/pickles/train_demo.pkl','wb+') as fp:
        pickle.dump([train3],fp)


    

    
