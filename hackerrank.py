# n=int(input())
# if(n<20):
#     if n %2 == 0:
#         print("Not Weird")
#     else:
#         print("Werid")

# else:
#     if n % 2 == 0:
#         print("Not Weird")
#     else:
#         print("Werid")

# def sudipta(s,i,k):
#     s[:i]+k+s[i+1:]
#     return 

# s="sudipta"
# i=2
# k="p"
# sp=sudipta(s,int(i),k)
# print(sp)

# def swap_case(s):
#     st=s.swapcase()
#     return st

# s = input()
# result = swap_case(s)
# print(result)

    
# N = int(input())
# L=[];
# for i in range(0,N):
#     cmd=input().split();
#     if cmd[0] == "insert":
#         L.insert(int(cmd[1]),int(cmd[2]))
#     elif cmd[0] == "append":
#         L.append(int(cmd[1]))
#     elif cmd[0] == "pop":
#         L.pop();
#     elif cmd[0] == "print":
#         print(L)
#     elif cmd[0] == "remove":
#         L.remove(int(cmd[1]))
#     elif cmd[0] == "sort":
#         L.sort();
#     else:
#         L.reverse();



# def count_substring(string, sub_string):
#     k=0
#     l=len(string)
#     l2=len(sub_string)
#     lt=[]
#     for i in range(l-2):
#         for j in range(i,l2+i):
#             lt.append(string[j])
#         if str(lt)==sub_string:
#             k+=1
#             lt.clear()
#         else:
#             k=k
#             lt.clear()

#     print(k)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# def count_substring(string, sub_string):
#     result=1
#     for i in range(len(string)-len(sub_string)):
#         if (string[i:i+len(sub_string)]==sub_string):
#             result+=1
#     return result
    

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(list(arr))



def transformSentence(sentence):
    l=sentence.split()
    
    li=[]
    st=""
    for i in l:
        st+=i[0]
        for j in range(0,len(i)-1):
            if(i[j].lower()<i[j+1].lower()):
                st+=(i[j+1].upper())
            elif(i[j].lower()>i[j+1].lower()):
                st+=(i[j+1].lower())
            else:
                st+=i[j+1]
        li.append(st)
        st=""
    result=""
    
    for i in li:
        result=result+" "+i
    return (result.strip())
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()