# scikit-learn algorithm cheat-sheet
import time


print("Strat")
time.sleep(1)

print(">50 samples")
choose = input("Enter Y or N ")
if choose == "N":
    print("----------------------------------------------------------")
    print("get more data")
    print("----------------------------------------------------------")
elif choose == "Y":
    print("")
    print("predicting a category")
    choose = input("Enter Y or N ")
    if choose == "N":
        print("")
        print("predicting a quantity")
        choose = input("Enter Y or N ")
        if choose == "N":
            print("")
            print("just looking")
            choose = input("Enter Y or N ")
            if choose =="N":
                print("----------------------------------------------------------")
                print("predicitng structure")
                time.sleep(1)
                print("tough luck")
                print("----------------------------------------------------------")
            elif choose == "Y":
                print("----------------------------------------------------------")
                print("Randomized PCA")
                print("----------------------------------------------------------")
                print("")
                choose = input("If it doesn't work, press Y. ")
                if choose =="Y":
                    print("")
                    print("<10K samples")
                    choose = input("Enter Y or N ")
                    if choose == "N":
                        print("----------------------------------------------------------")
                        print("kernel approximation")
                        print("----------------------------------------------------------")
                    elif choose == "Y":
                        print("----------------------------------------------------------")
                        print("Isomap")
                        print("Spectral Embedding")
                        print("----------------------------------------------------------")
                        print("")
                        choose = input("If it doesn't work, press Y. ")
                        if choose == "Y":
                            print("----------------------------------------------------------")
                            print("LLE")
                            print("----------------------------------------------------------")
        elif choose == "Y":
            print("")
            print("<100K samples")
            choose = input("Enter Y or N ")
            if choose == "N":
                print("----------------------------------------------------------")
                print("SGD Regressor")
                print("----------------------------------------------------------")
            elif choose == "Y":
                print("")
                print("few features should be important")
                choose = input("Enter Y or N ")
                if choose == "N":
                    print("----------------------------------------------------------")
                    print("RidgeRegression")
                    print("SVR(kernel=\'linear\')")
                    print("----------------------------------------------------------")
                    print("")
                    choose = input("If it doesn't work, press Y. ")
                    if choose == "Y":
                        print("----------------------------------------------------------")
                        print("SVR(kernel=\'rbf\')")
                        print("EnsembleRegressors")
                        print("----------------------------------------------------------")
                elif choose =="Y":
                    print("----------------------------------------------------------")
                    print("Lasso")
                    print("ElasticNet")
                    print("----------------------------------------------------------")
    elif choose == "Y":
        print("")
        print("do you have labeled data")
        choose = input("Enter Y or N ")
        if choose == "N":
            print("")
            print("number of categories Known")
            choose = input("Enter Y or N ")
            if choose == "N":
                print("")
                print("<10K samples")
                choose = input("Enter Y or N ")
                if choose == "N":
                    print("----------------------------------------------------------")
                    print("tough luck")
                    print("----------------------------------------------------------")
                elif choose == "Y":
                    print("----------------------------------------------------------")
                    print("MeanShift")
                    print("VBGMM")
                    print("----------------------------------------------------------")
            elif choose == "Y":
                print("")
                print("<10K samples")
                choose = input("Enter Y or N ")
                if choose == "N":
                    print("----------------------------------------------------------")
                    print("MiniBath Kmeans")
                    print("----------------------------------------------------------")
                elif choose == "Y":
                    print("----------------------------------------------------------")
                    print("KMeans")
                    print("----------------------------------------------------------")
                    f = open("./Kmeans.py", "w")
                    code = "#Import Library\nfrom sklearn.cluster import Kmeans\n#Assumed you have, X for training data set\n#and x_test of test_dataset\n#Create KNeighbors classifier object model\nk_means = KMeans(n_clusters=3, random_stat=0)\n#Train the model using the training sets and check score\nmodel.fit(X)\n#predict output\npredicted = model.predict(x_test)"
                    f.write(code)
                    f.close()
                    print("")
                    choose = input("If it doesn't work, press Y. ")
                    if choose == "Y":
                        print("----------------------------------------------------------")
                        print("Spectral Clustreing")
                        print("GMM")
                        print("----------------------------------------------------------")
        elif choose == "Y":
            print("")
            print("<100K samples")
            choose = input("Enter Y or N ")
            if choose == "N":
                print("----------------------------------------------------------")
                print("SGD Classifier")
                print("----------------------------------------------------------")
                print("")
                choose = input("If it doesn't work, press Y. ")
                if choose == "Y":
                    print("----------------------------------------------------------")
                    print("kernel approximation")
                    print("----------------------------------------------------------")
            elif choose == "Y":
                print("----------------------------------------------------------")
                print("Linear SVC")
                print("----------------------------------------------------------")
                print("")
                choose = input("If it doesn't work, press Y. ")
                if choose == "Y":
                    print("")
                    print("Text Data")
                    choose = input("Enter Y or N ")
                    if choose == "N":
                        print("----------------------------------------------------------")
                        print("KNeighbors Classifier")
                        print("----------------------------------------------------------")
                        print("")
                        choose = input("If it doesn't work, press Y. ")
                        if choose == "Y":
                            print("----------------------------------------------------------")
                            print("SVC")
                            print("Ensemble Classifiers")
                            print("----------------------------------------------------------")
                    elif choose == "Y":
                        print("----------------------------------------------------------")
                        print("Naive Bayes")
                        print("----------------------------------------------------------")


time.sleep(9999)
