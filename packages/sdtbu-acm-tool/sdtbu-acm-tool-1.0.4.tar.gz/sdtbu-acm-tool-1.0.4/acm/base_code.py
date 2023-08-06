{
  "3811": {
    "sid": 2484305,
    "code": "C++",
    "content": "#include<stdio.h>\r\n\r\nvoid plus(int *p1,int *p2,int *p3) \r\n\r\n{\r\n\t*p3=*p2*(*p1);\r\n} \r\n\r\nint main() \r\n\r\n{ int a,b,*p1,*p2; \r\n\r\n a=10;\r\n\r\n b=20;\r\n\r\n p1=&a; \r\n\r\n  p2=&b; \r\n\r\n  plus(p1,p2,&a);\t\r\n\r\n  printf(\"%d\",a); \r\n\r\n  return 0; } "
  },
  "2055": {
    "sid": 2484301,
    "code": "C",
    "content": "#include \"stdio.h\"\r\n#include <stdlib.h>\r\n#define STACK_INIT_SIZE 100\r\n#define STACKINCREMENT 10\r\n#define QUEEN_SIZE 50\r\ntypedef int ElemType;\r\n\r\n//\u961f\u5217\u7ed3\u6784\u4f53\r\ntypedef struct SqQueue {\r\n    ElemType front; //\u961f\u5934\u6307\u9488\r\n    ElemType rear; //\u961f\u5c3e\u6307\u9488\r\n    ElemType data[QUEEN_SIZE];\r\n} SeqQueue;\r\n\r\n//\u961f\u5217\u7684\u521d\u59cb\u5316\r\nvoid InitQueue(SeqQueue *Q){\r\n    Q->front = Q->rear = 0;\r\n}\r\n\r\n//\u961f\u5217\u662f\u5426\u4e3a\u7a7a\r\nint QueueEmpty(SeqQueue *Q){\r\n    if(Q->front == Q->rear){\r\n        return 1;\r\n    }\r\n    return 0;\r\n}\r\n\r\n//\u961f\u5217\u662f\u5426\u5df2\u6ee1\r\nint QueueFull(SeqQueue *Q){\r\n    if((Q->rear+1)%QUEEN_SIZE == Q->front){\r\n        return 1;\r\n    }\r\n    return 0;\r\n}\r\n\r\n//\u961f\u5217\u7684\u5165\u961f\r\nvoid EnQueue(SeqQueue *Q, ElemType e){\r\n    if((Q->rear + 1) % QUEEN_SIZE == Q->front){\r\n        return;\r\n    }\r\n    Q->data[Q->rear] = e;\r\n    Q->rear = (Q->rear + 1) % QUEEN_SIZE;\r\n}\r\n\r\n//\u961f\u5217\u7684\u51fa\u961f\r\nvoid DeQueue(SeqQueue *Q, ElemType *e){\r\n    if(Q->front == Q->rear){\r\n        return;\r\n    }\r\n    *e = Q->data[Q->front];\r\n    Q->front = (Q->front + 1) % QUEEN_SIZE;\r\n}\r\n\r\n//\u6808\u7ed3\u6784\u4f53\r\ntypedef struct SqStack {\r\n    ElemType *base; //\u6808\u5e95\u6307\u9488\r\n    ElemType *top; //\u6808\u9876\u6307\u9488\r\n    int stacksize; //\u5f53\u524d\u5df2\u5206\u914d\u7684\u5b58\u50a8\u7a7a\u95f4\uff0c\u4ee5\u5143\u7d20\u4e3a\u5355\u4f4d\r\n} SeqStack;\r\n\r\n//\u6808\u7684\u521d\u59cb\u5316\r\nSeqStack *InitStack(SeqStack *S) {\r\n    S = (SeqStack *) malloc(sizeof(SeqStack));\r\n    S->base = (ElemType *) malloc(STACK_INIT_SIZE * sizeof(ElemType));\r\n    if (!S->base) {\r\n        exit(0);\r\n    }\r\n    S->top = S->base;\r\n    S->stacksize = STACK_INIT_SIZE;\r\n    return S;\r\n}\r\n\r\n//\u6808\u7684\u5165\u6808\r\nvoid Push(SeqStack *S, ElemType e) {\r\n    if (S->top - S->base >= S->stacksize) {\r\n        S->base = (ElemType *) realloc(S->base, (S->stacksize + STACKINCREMENT) * sizeof(ElemType));\r\n        if (!S->base) {\r\n            exit(0);\r\n        }\r\n        S->top = S->base + S->stacksize;\r\n        S->stacksize += STACKINCREMENT;\r\n    }\r\n    *S->top = e;\r\n    S->top++;\r\n}\r\n\r\n//\u6808\u7684\u51fa\u6808\r\nvoid Pop(SeqStack *S, ElemType *e) {\r\n    if (S->top == S->base) {\r\n        return;\r\n    }\r\n    --S->top;\r\n    *e = *S->top;\r\n}\r\n\r\n//\u6808\u7684\u5224\u7a7a\r\nint StackEmpty(SeqStack *S) {\r\n    if (S->top == S->base) {\r\n        return 1;\r\n    } else {\r\n        return 0;\r\n    }\r\n}\r\n\r\n//\u6808\u7684\u5224\u6ee1\r\nint StackFull(SeqStack *S) {\r\n    if (S->top - S->base >= S->stacksize) {\r\n        return 1;\r\n    } else {\r\n        return 0;\r\n    }\r\n}\r\n\r\n//\u6808\u7684\u904d\u5386\r\nvoid StackTraverse(SeqStack *S) {\r\n    ElemType *p;\r\n    p = S->top;\r\n    while (p > S->base) {\r\n        p--;\r\n        if (p == S->base)\r\n            printf(\"%d \", *p);\r\n        else\r\n            printf(\"%d \", *p);\r\n    }\r\n}\r\n\r\nint main()\r\n{\r\n    ElemType n,temp;\r\n    SeqQueue *Q = (SeqQueue *)malloc(sizeof(SeqQueue));\r\n    SeqStack *S = NULL;\r\n    InitQueue(Q);\r\n    S=InitStack(S);\r\n    scanf(\"%d\", &n);\r\n    for (int i = 0; i < n; i++)\r\n    {\r\n        scanf(\"%d\", &temp);\r\n        EnQueue(Q, temp);\r\n    }\r\n    for (int i = 0; i < n; ++i) {\r\n        Push(S, Q->data[i]);\r\n    }\r\n    StackTraverse(S);\r\n    return 0;\r\n}\r\n\r\n\r\n"
  },
  "2639": {
    "sid": 2484300,
    "code": "C",
    "content": "#include \"stdio.h\"\r\n#include <stdlib.h>\r\n#define STACK_INIT_SIZE 100\r\n#define STACKINCREMENT 10\r\ntypedef char ElemType;\r\n\r\n//\u6808\u7ed3\u6784\u4f53\r\ntypedef struct SqStack {\r\n    ElemType *base; //\u6808\u5e95\u6307\u9488\r\n    ElemType *top; //\u6808\u9876\u6307\u9488\r\n    int stacksize; //\u5f53\u524d\u5df2\u5206\u914d\u7684\u5b58\u50a8\u7a7a\u95f4\uff0c\u4ee5\u5143\u7d20\u4e3a\u5355\u4f4d\r\n} SeqStack;\r\n\r\n//\u6808\u7684\u521d\u59cb\u5316\r\nSeqStack *InitStack(SeqStack *S) {\r\n    S = (SeqStack *) malloc(sizeof(SeqStack));\r\n    S->base = (ElemType *) malloc(STACK_INIT_SIZE * sizeof(ElemType));\r\n    if (!S->base) {\r\n        exit(0);\r\n    }\r\n    S->top = S->base;\r\n    S->stacksize = STACK_INIT_SIZE;\r\n    return S;\r\n}\r\n\r\n//\u6808\u7684\u5165\u6808\r\nvoid Push(SeqStack *S, ElemType e) {\r\n    if (S->top - S->base >= S->stacksize) {\r\n        S->base = (ElemType *) realloc(S->base, (S->stacksize + STACKINCREMENT) * sizeof(ElemType));\r\n        if (!S->base) {\r\n            exit(0);\r\n        }\r\n        S->top = S->base + S->stacksize;\r\n        S->stacksize += STACKINCREMENT;\r\n    }\r\n    *S->top = e;\r\n    S->top++;\r\n}\r\n\r\n//\u6808\u7684\u51fa\u6808\r\nvoid Pop(SeqStack *S, ElemType *e) {\r\n    if (S->top == S->base) {\r\n        return;\r\n    }\r\n    --S->top;\r\n    *e = *S->top;\r\n}\r\n\r\n//\u6808\u7684\u9500\u6bc1\r\nvoid DestroyStack(SeqStack *S) {\r\n    free(S->base);\r\n    free(S);\r\n}\r\n\r\n//\u6808\u7684\u6e05\u7a7a\r\nvoid ClearStack(SeqStack *S) {\r\n    S->top = S->base;\r\n}\r\n\r\n//\u6808\u7684\u5224\u7a7a\r\nint StackEmpty(SeqStack *S) {\r\n    if (S->top == S->base) {\r\n        return 1;\r\n    } else {\r\n        return 0;\r\n    }\r\n}\r\n\r\n//\u53d6\u6808\u9876\u5143\u7d20\r\nvoid GetTop(SeqStack *S, ElemType *e) {\r\n    if (S->top == S->base) {\r\n        return;\r\n    }\r\n    *e = *(S->top - 1);\r\n}\r\n\r\n//\u6808\u7684\u904d\u5386\r\nvoid StackTraverse(SeqStack *S) {\r\n    ElemType *p;\r\n    p = S->top;\r\n    while (p > S->base) {\r\n        p--;\r\n        printf(\"%d \", *p);\r\n    }\r\n}\r\n\r\n//\u62ec\u53f7\u5339\u914d\u95ee\u9898\r\nint BracketMatch(char *str) {\r\n    SeqStack *S = NULL;\r\n    char *p;\r\n    char e;\r\n    S = InitStack(S);\r\n    p = str;\r\n    while (*p != '\\0') {\r\n        switch (*p) {\r\n            case '(':\r\n            case '[':\r\n            case '{':\r\n                Push(S, *p);\r\n                break;\r\n            case ')':\r\n                GetTop(S, &e);\r\n                if (e == '(') {\r\n                    Pop(S, &e);\r\n                } else {\r\n                    return 0;\r\n                }\r\n                break;\r\n            case ']':\r\n                GetTop(S, &e);\r\n                if (e == '[') {\r\n                    Pop(S, &e);\r\n                } else {\r\n                    return 0;\r\n                }\r\n                break;\r\n            case '}':\r\n                GetTop(S, &e);\r\n                if (e == '{') {\r\n                    Pop(S, &e);\r\n                } else {\r\n                    return 0;\r\n                }\r\n                break;\r\n        }\r\n        p++;\r\n    }\r\n    if (StackEmpty(S)) {\r\n        return 1;\r\n    } else {\r\n        return 0;\r\n    }\r\n}\r\n\r\nint main()\r\n{\r\n    char str[100];\r\n    scanf(\"%s\", str);\r\n    if (BracketMatch(str)) {\r\n        printf(\"YES\");\r\n    } else {\r\n        printf(\"NO\");\r\n    }\r\n    return 0;\r\n}\r\n\r\n\r\n\r\n"
  },
  "3829": {
    "sid": 2483809,
    "code": "C++",
    "content": "#include<stdio.h>\r\nvoid add(int *p1,int *p2)\r\n{\r\n\t*p1=*p1+*p2;\r\n\t\r\n}\r\nint main()\r\n{\r\n\tint a,b,*p1,*p2;a=10;b=20;\r\n\tp1=&a;\r\n\tp2=&b;\r\n\tadd(p1,p2);\r\n\tprintf(\"%d\",a);\r\n\treturn 0;\t\r\n} "
  },
  "3081": {
    "sid": 2483808,
    "code": "C",
    "content": "#include <stdio.h>\r\nint main() {\r\n\tchar a[100];\r\n    int i, in_word, word_num;\r\n    gets(a);\r\n    word_num = 0; \r\n    in_word = 0; \r\n        for (i = 0; a[i]; i++)\r\n            {\r\n        if (a[i] == ' ') \r\n            { \r\n            in_word = 0; \r\n        } \r\n        else if (in_word == 0)\r\n            { \r\n            word_num++; \r\n            in_word = 1; \r\n        }\r\n    }\r\n    printf(\"%d\", word_num);\r\n}\r\n"
  },
  "3844": {
    "sid": 2483806,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n\r\nint main()\r\n{\r\n   int a,b,c,d;\r\n   scanf(\"%d %d\",&a,&b);\r\n\r\n   c=a-b;\r\n   d=a*b;\r\n   if(c>=0)\r\n    printf(\"%d %d\",c,d);\r\n   else\r\n    printf(\"%d %d\",-c,d);\r\n\r\n   return 0;\r\n\r\n}"
  },
  "3873": {
    "sid": 2483805,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\nint main()\r\n{\r\n    int i;\r\n    scanf(\"%d\",&i);\r\n    printf(\"%d%d%d\",i%10,i/10%10,i/100);\r\n    return 0;\r\n}"
  },
  "3852": {
    "sid": 2483804,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\nint jug(int year);//\u51fd\u65701\u58f0\u660e\r\nvoid range(int m,int n);//\u51fd\u65702\u58f0\u660e\r\nint main()\r\n{\r\n   int m,n;\r\n   scanf(\"%d %d\",&m,&n);\r\n   range(m,n);\r\n   return 0;\r\n}\r\n\r\nint jug(int year)//\u51fd\u6570\u4e00\uff1a\u5224\u65ad\u95f0\u5e74\r\n{\r\n    int ret;\r\n    if((year%4==0&&year%100!=0)||year%400==0){\r\n      ret=1;\r\n    }\r\n    else{\r\n      ret=0;\r\n    }\r\n    return ret;\r\n}\r\n\r\nvoid range(int m,int n)//\u51fd\u65702\uff1a\u8303\u56f4\u5e76\u8f93\u51fa\r\n{\r\n    int year;\r\n    for(year=m;year<=n;year++){\r\n        if(jug(year)){\r\n            printf(\"%d \",year);\r\n        }\r\n    }\r\n}"
  },
  "3739": {
    "sid": 2483803,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n\r\nint main()\r\n{\r\n   int i,number=0,a;\r\n   for(i=1;i<=5;i++){\r\n    scanf(\"%d\",&a);\r\n    switch(a){\r\n    case 1: number+=3;break;\r\n    case 2: number+=6;break;\r\n    case 3: number+=5;break;\r\n    case 4: number+=4;break;\r\n    case 5: number+=4;break;\r\n    case 6: number+=7;break;\r\n    case 7: number+=8;break;\r\n    case 8: number+=2;break;\r\n    case 9: number+=2;break;\r\n    case 10: number+=6;break;\r\n    }\r\n   }\r\n   if(number>=30){\r\n    printf(\"hard\");\r\n   }\r\n   else if(number<30&&number>=20){\r\n    printf(\"normal\");\r\n   }\r\n   else{\r\n    printf(\"easy\");\r\n   }\r\n   return 0;\r\n}"
  },
  "3876": {
    "sid": 2483802,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n\r\nint main()\r\n{\r\n    int i,j,n;\r\n    int sum=0;\r\n    scanf(\"%d\",&n);\r\n    for(i=1;i<=n;i++){\r\n            sum=0;\r\n        for(j=1;j<i;j++){\r\n            if(i%j==0){\r\n                sum+=j;\r\n            }\r\n        }\r\n        if(sum==i){\r\n            printf(\"%d\\n\",i);\r\n        }\r\n    }\r\n    return 0;\r\n}"
  },
  "1221": {
    "sid": 2483800,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\nint juge(int n)\r\n{\r\n    int i;\r\n    int ret=1;\r\n    for(i=2;i*i<=n;i++){\r\n        if(n%i==0){\r\n            ret=0;\r\n            break;\r\n        }\r\n    }\r\n    return ret;\r\n}\r\nint main()\r\n{\r\n    int n,i,j;\r\n    int cot=0;\r\n    for(i=1;i++;){\r\n       scanf(\"%d\",&n);\r\n       if(n==0){\r\n        break;\r\n       }\r\n         for(j=2;j<=n/2;j++){\r\n            if(juge(j)&&juge(n-j)){\r\n                cot++;\r\n            }\r\n         }\r\n         printf(\"%d\\n\",cot);\r\n         cot=0;\r\n    }\r\n\r\n    return 0;\r\n}"
  },
  "1922": {
    "sid": 2483799,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\nvoid hano(int n,char one,char two,char three)\r\n{\r\n    if(n>=2){\r\n    hano(n-1,one,three,two);\r\n    printf(\"Move disk %d from %c to %c\\n\",n,one,three);\r\n    hano(n-1,two,one,three);\r\n    }\r\n    else\r\n        printf(\"Move disk %d from %c to %c\\n\",n,one,three);\r\n}\r\nint main()\r\n{\r\n    int n;\r\n    char A,B,C;\r\n\r\n    scanf(\"%d\",&n);\r\n    hano(n,'A','B','C');\r\n    return 0;\r\n}"
  },
  "3074": {
    "sid": 2483798,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n\r\nint main()\r\n{\r\n    double a[10000],sum=0;\r\n    double n;\r\n    scanf(\"%lf\",&n);\r\n    int i,j,t;\r\n\r\n    for(i=0;i<n;i++){\r\n        scanf(\"%lf\",&a[i]);\r\n    }//!\u8f93\u5165\u5206\u6570\r\n    for(i=0;i<n;i++){\r\n        for(j=0;j<n-1;j++){\r\n            if(a[j]<a[j+1]){\r\n                t=a[j];\r\n                a[j]=a[j+1];\r\n                a[j+1]=t;\r\n            }\r\n        }\r\n    }//!\u5192\u6ce1\u6392\u5e8f\uff0c\u6700\u5927\u6700\u5c0f\u5728\u9996\u5c3e\r\n    for(i=1;i<n-1;i++){\r\n        sum+=a[i];\r\n    }\r\n    printf(\"%.2f\\n\",sum/(n-2.0));\r\n\r\n    return 0;\r\n}"
  },
  "3076": {
    "sid": 2483797,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n\r\nint main()\r\n{\r\n    int a[10];\r\n    int i,j,x,t;\r\n\r\n    for(i=0;i<9;i++){\r\n        scanf(\"%d\",&a[i]);\r\n    }\r\n    scanf(\"%d\",&x);\r\n    for(i=0;i<9;i++){\r\n        if(x>=a[0]){\r\n            for(j=9;j>0;j--){\r\n                a[j]=a[j-1];\r\n            }\r\n            a[0]=x;\r\n            break;\r\n        }\r\n        else if(x<=a[8]){\r\n            a[9]=x;\r\n            break;\r\n        }\r\n        else{\r\n            if(x<a[i]&&x>a[i+1]){\r\n                for(j=9;j>(i+1);j--){\r\n                    a[j]=a[j-1];\r\n                }\r\n                a[i+1]=x;\r\n                break;\r\n            }\r\n        }\r\n    }\r\n    for(i=0;i<10;i++){\r\n        if(i!=9){\r\n            printf(\"%d \",a[i]);\r\n        }\r\n        else{\r\n            printf(\"%d\\n\",a[i]);\r\n        }\r\n    }\r\n\r\n    return 0;\r\n}"
  },
  "4202": {
    "sid": 2483796,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n#include <string.h>\r\n\r\nint main()\r\n{\r\n    long long n,s;\r\n    scanf(\"%lld\",&n);\r\n    s=n+(n*(n-1))/2;\r\n    printf(\"%lld\",s);\r\n\r\n    return 0;\r\n}"
  },
  "1930": {
    "sid": 2483596,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat C,F;\r\n\tscanf(\"%f\",&F);\r\n\tC=5*(F-32)/9;\r\n\tprintf(\"%.2f\",C);\r\n\t\r\n}"
  },
  "3620": {
    "sid": 2483595,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat a,b,c,p,s;\r\n\tscanf(\"%f %f %f\",&a,&b,&c);\r\n\tp=(a+b+c)/2;\r\n\ts=sqrt(p*(p-a)*(p-b)*(p-c));\r\n\tprintf(\"%.2f\",s);\r\n\t\r\n}"
  },
  "3738": {
    "sid": 2483594,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,d,e,f,m;\r\n\tscanf(\"%d,%d,%d\",&a,&b,&c);\r\n\td=a+b+c;\r\n\t\r\n\te=a;\r\n\tif(e<b)\r\n\te=b;\r\n\tif(e<c)\r\n\te=c;\r\n\t\r\n\tf=a;\r\n\tif(f>b)\r\n\tf=b;\r\n\tif(f>c)\r\n\tf=c;\r\n\t\r\n\tm=d-e-f;\r\n\tprintf(\"%d,%d,%d\",e,f,m);\r\n\t\r\n}"
  },
  "3041": {
    "sid": 2483593,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tif(a%35==0)\r\n\tprintf(\"yes\");\r\n\telse\r\n\tprintf(\"no\");\r\n\t\r\n}"
  },
  "1911": {
    "sid": 2483592,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a,b,c,d,t;\r\n\tscanf(\"%d\",&a);\r\n\tb=a/100;\r\n\tc=(a-b*100)/10;\r\n\td=(a-b*100-c*10);\r\n\tif(d==0){\r\n\t\tif(c==0)\r\n\t\tt=b;\r\n\t\telse\r\n\t\tt=c*10+b;\r\n\t}\r\n\r\n\telse\r\n\tt=d*100+c*10+b;\r\n\tprintf(\"%d\",t);\r\n\t\r\n}"
  },
  "1883": {
    "sid": 2483591,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat a,c,d,b,x1,x2,x;\r\n\tscanf(\"%f %f %f\",&a,&b,&c);\r\n\td=b*b-4*a*c;\r\n \tif(d>=0){\r\n\t\tx1=(-b+sqrt(d))/2/a;\r\n\t\tx2=(-b-sqrt(d))/2/a;\r\n\t\tprintf(\"%.2f %.2f\",x1,x2);\r\n \t}\r\n}"
  },
  "1914": {
    "sid": 2483589,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat a,c,d,b,x1,x2,x,x3,x4;\r\n\tscanf(\"%f %f %f\",&a,&b,&c);\r\n\td=b*b-4*a*c;\r\n \tif(d>=0){\r\n\t\tx1=(-b+sqrt(d))/2/a;\r\n\t\tx2=(-b-sqrt(d))/2/a;\r\n\t\tprintf(\"%.2f %.2f\",x1,x2);\r\n \t}\r\n\telse\r\n\t{\r\n\t\tx1=-b/2/a;x3=sqrt(-d)/2/a;\r\n\t\tx2=-b/2/a;x4=sqrt(-d)/2/a;\r\n\t\tprintf(\"%.2f+%.2fi %.2f-%.2fi\",x1,x3,x2,x4);\r\n\t}\r\n}"
  },
  "3614": {
    "sid": 2483586,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,a[11][11],i,j,sum=0;\r\n\tscanf(\"%d\\n\",&n);\r\n\tfor(i=0;i<n;i++){\r\n\t\tfor(j=0;j<n;j++){\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tif(a[i][j]%2==1){\r\n\t\t\t\tsum+=a[i][j];\r\n\t\t\t}\t\r\n\t\t}\t\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "3632": {
    "sid": 2483585,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h>\r\n\r\nint f1(int n){\r\n\tif(n != 1){\r\n\t\treturn (2*n-1)*(2*n-1)+f1(n-1);\r\n\t}\r\n\tif(n==1){\r\n\t\treturn 1;\r\n\t}\r\n}\r\n\r\nint main()\r\n\r\n{\r\n\r\n    int sum;\r\n\r\n    int i,n;\r\n\r\n    scanf(\"%d\",&n);\t\t\r\n\r\n    sum=f1(n);\r\n\r\n    printf(\"%d\",sum);\r\n\r\n    return 0;\r\n\r\n}"
  },
  "2524": {
    "sid": 2483583,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[11],m,t,i,book=0;\r\n\tscanf(\"%d %d %d %d %d %d %d %d %d %d\\n%d\",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9],&m);\r\n\tt=m+30;\r\n\tfor(i=0;i<10;i++){\r\n\t\tif(a[i]<=t){\r\n\t\t\tbook++;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",book);\r\n\t\r\n}"
  },
  "2905": {
    "sid": 2483581,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"Mabinogi\");\r\n}"
  },
  "1563": {
    "sid": 2483579,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\twhile(scanf(\"%x %x\",&a,&b)!=EOF\t){\r\n\t\tprintf(\"%d\\n\",a+b);\r\n\t}\r\n\t\r\n}"
  },
  "3784": {
    "sid": 2483578,
    "code": "C",
    "content": "#include<stdio.h>\r\nint f(int i){\r\n\tif(i==1||i==2){\r\n\t\treturn 1;\r\n\t}else{\r\n\t\treturn f(i-1)+f(i-2);\r\n\t}\r\n}\r\nint main(){\r\n\tint a,i;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=1;i<a;i++){\r\n\t\tprintf(\"%d,\",f(i));\r\n\t}printf(\"%d\",f(i));\r\n}"
  },
  "1869": {
    "sid": 2483577,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint\t main(){\r\n\tint a[101],i,n,max=0;\r\n\tscanf(\"%d\\n\",&n);\r\n\tfor(i=0;i<n;i++){\r\n\t\tscanf(\"%d\\n\",&a[i]);\r\n\t\tif(fabs(max)<fabs(a[i])){\r\n\t\t\tmax=a[i];\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",max);\t\r\n}"
  },
  "3894": {
    "sid": 2483575,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n\tint a[10],i,max=0,min=999,sum=0;\r\n\tdouble t;\r\n\tfor(i=0;i<10;i++){\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t\tif(a[i]>max){\r\n\t\t\tmax=a[i];\r\n\t\t}if(a[i]<min){\r\n\t\t\tmin=a[i];\r\n\t\t}sum+=a[i];\r\n\t}sum-=max+min;\r\n\tt=(double)sum/8.0;\r\n\tprintf(\"%.2lf\",t);\r\n}"
  },
  "3299": {
    "sid": 2483574,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n\tlong int a,b,c,d,n,i,min=0;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++){\r\n\t\tscanf(\"%ld %ld %ld %ld\",&a,&b,&c,&d);\r\n\t\tmin=a;\r\n\t\tif(b<min){\r\n\t\t\tmin=b;\r\n\t\t}if(c<min){\r\n\t\t\tmin=c;\r\n\t\t}if(d<min){\r\n\t\t\tmin=d;\r\n\t\t}\r\n\t\tprintf(\"The minimum number is %ld.\\n\",min);\r\n\t}\r\n}"
  },
  "2772": {
    "sid": 2483573,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h>\r\nint f(int x,int y,int *p){\r\n\t*p= x;\r\n\treturn y;\r\n}\r\nint main(){\r\n\tint a,b,p;\r\n\tscanf(\"%d %d\",&a,&b);\r\n\ta=f(a,b,&p),b=p;\r\n\tprintf(\"%d %d\",a,b);\r\n\treturn 0;\r\n}"
  },
  "2774": {
    "sid": 2483572,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n\tint a[5][5],b,c,sum=0,n,i,j;\r\n\tfor(i=0;i<5;i++){\r\n\t\tfor(j=0;j<5;j++){\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tif(i+j<=4){\r\n\t\t\t\tsum+=a[i][j];\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "2783": {
    "sid": 2483570,
    "code": "C",
    "content": "#include<stdio.h>\r\nint f(int i){\r\n\tint a,b,c,t;\r\n\tif(i==1000||i==100||i==10||i==1){\r\n\t\treturn 1;\r\n\t}if(i>100){\r\n\t\ta=i%10;\r\n\t\tb=(i%100-a)/10;\r\n\t\tc=i/100;\r\n\t\tt=a+b+c;\r\n\t\treturn f(t);\r\n\t}if(i>10){\r\n\t\ta=i%10;\r\n\t\tb=(i%100-a)/10;\r\n\t\tt=a+b;\r\n\t\treturn f(t);\r\n\t}else{\r\n\t\treturn i;\r\n\t}\r\n}\r\nint main(){\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tprintf(\"%d\",f(a));\r\n}"
  },
  "3870": {
    "sid": 2483568,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n\tint a,i,c=0;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=0;c<a;i++){\r\n\t\tif(i%3==2&&i%5==3&&i%7==4){\r\n\t\t\tprintf(\"%d\\n\",i);\r\n\t\t\tc++;\r\n\t\t}\r\n\t}\r\n\t\r\n}"
  },
  "3764": {
    "sid": 2483567,
    "code": "C",
    "content": "#include<stdio.h>\r\nint f(int a,int b){\r\n\tint m,n;\r\n\tm=a,n=b;\r\n\tif(a<b){\r\n\t\tm=b,n=a;\r\n\t}\r\n\tif(m%n==0){\r\n\t\treturn n;\r\n\t}else{\r\n\t\tint c=m%n;\r\n\t\treturn f(n,c);\r\n\t}\r\n} \r\nint  main(){\r\n\tlong int a,b;\r\n\tscanf(\"%ld,%ld\",&a,&b);\r\n\tprintf(\"%ld\",a*b/f(a,b));\r\n}"
  },
  "2012": {
    "sid": 2481697,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <string.h>\r\n\r\nint isPalindrome(char string[]) {\r\n    int i = 0;\r\n    int j = strlen(string) - 1;\r\n    while (i < j) {\r\n        if (string[i] != string[j]) {\r\n            return 0;\r\n        }\r\n        i++;\r\n        j--;\r\n    }\r\n    return 1;\r\n}\r\nint main() {\r\n    int num;\r\n    scanf(\"%d\", &num);\r\n    for (int i = 0; i < num; ++i) {\r\n        char string[100];\r\n        scanf(\"%s\", string);\r\n        if (isPalindrome(string)) {\r\n            printf(\"YES\");\r\n        } else {\r\n            printf(\"NO\");\r\n        }\r\n        if(i != num - 1) {\r\n            printf(\"\\n\");\r\n        }\r\n    }\r\n}\r\n"
  },
  "2791": {
    "sid": 2481696,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <math.h>\r\n\r\ndouble get_num(int num){\r\n    double num_return;\r\n    int sige = (int)pow((-1),num)*(-1);\r\n    num_return = (1.0/num) * sige;\r\n    return num_return;\r\n}\r\n\r\ndouble change_num(int n){\r\n    double temp=0;\r\n    for (int i = 1; i <= n; ++i) {\r\n        temp += get_num(i);\r\n    }\r\n    return temp;\r\n}\r\n\r\nint main() {\r\n    int m;\r\n    scanf(\"%d\",&m);\r\n    int ls[m];\r\n    double ls_1[m];\r\n    for (int i = 0; i < m; ++i) {\r\n        scanf(\"%d\",&ls[i]);\r\n    }\r\n    for (int i = 0; i < m; ++i) {\r\n        ls_1[i] = change_num(ls[i]);\r\n    }\r\n    for (int i = 0; i < m; ++i) {\r\n        printf(\"%.2lf\\n\",ls_1[i]);\r\n    }\r\n}\r\n\r\n"
  },
  "2788": {
    "sid": 2481695,
    "code": "C",
    "content": "#include <stdio.h>\r\n\r\nint main() {\r\n    int n;\r\n    scanf(\"%d\",&n);\r\n    int ls[n];\r\n    for (int i = 0; i < n; ++i) {\r\n        scanf(\"%d\",&ls[i]);\r\n    }\r\n\r\n    for (int i = 0; i < n; ++i) {\r\n        for (int j = i; j < n; ++j) {\r\n            if(ls[i]>ls[j]){\r\n                int temp = ls[i];\r\n                ls[i] = ls[j];\r\n                ls[j] = temp;\r\n            }\r\n        }\r\n    }\r\n    for (int i = 0; i < n; ++i) {\r\n        printf(\"%d\\n\",ls[i]);\r\n    }\r\n}\r\n"
  },
  "2786": {
    "sid": 2481694,
    "code": "C",
    "content": "#include <stdio.h>\r\n\r\nint main() {\r\n    int a = 1,b = 1;\r\n    int temp;\r\n    printf(\"1\\n1\\n\");\r\n    for (int i = 0; i < 38; ++i) {\r\n        temp = a + b;\r\n        printf(\"%d\\n\",temp);\r\n        b = a;\r\n        a = temp;\r\n    }\r\n}\r\n"
  },
  "2785": {
    "sid": 2481693,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n    int a=1;\r\n    while(!(a%2==1&&a%3==2&&a%5==4&&a%6==5&&a%7==0)){\r\n        a++;\r\n    }\r\n    printf(\"%d\",a);\r\n}"
  },
  "3760": {
    "sid": 2481687,
    "code": "Python",
    "content": "a = int(input())\r\na1 = a % 10\r\na2 = (a % 100 - a1) / 10\r\na3 = (a % 1000 - a2 * 10 - a1) / 100\r\na4 = (a - a3 * 100 - a2 * 10 - a1) / 1000\r\nprint(str(int(a4))+','+str(int(a3))+','+str(int(a2))+','+str(int(a1)),end='')"
  },
  "3815": {
    "sid": 2481686,
    "code": "Python",
    "content": "print('*********',end='')"
  },
  "3816": {
    "sid": 2481685,
    "code": "Python",
    "content": "print('*********\\n*********\\n*********',end='')"
  },
  "3864": {
    "sid": 2481684,
    "code": "Python",
    "content": "a = input()\r\nb = a.find(',')\r\na1 = int(a[:b])\r\na2 = int(a[b+1:])\r\n\r\n\r\ny = a2/2 - a1\r\nx = a1 - y\r\n\r\nprint(str(int(x))+','+str(int(y)))\r\n"
  },
  "3819": {
    "sid": 2481683,
    "code": "Python",
    "content": "print('  *\\n ***\\n*****\\n ***\\n  * ',end='')"
  },
  "3818": {
    "sid": 2481682,
    "code": "Python",
    "content": "print('  *\\n ***\\n*****')"
  },
  "1880": {
    "sid": 2481681,
    "code": "Python",
    "content": "a = input()\r\ntemp = a.find(' ')\r\na_1 = int(a[:temp])\r\na_2 = int(a[temp+1:])\r\n\r\nif a_1>a_2:\r\n    MAX = a_1\r\nelse:\r\n    MAX = a_2\r\n\r\nprint(\"max=\"+str(MAX),end='')"
  },
  "1871": {
    "sid": 2481680,
    "code": "Python",
    "content": "def f(m,n):\r\n    if m==1:\r\n        return n\r\n    elif n==1:\r\n        return m\r\n    elif (m>1)&(n>1):\r\n        return f(m-1,n) + f(m,n-1)\r\n\r\nls_1 = []\r\nls_2 = []\r\nn = int(input())\r\nfor i in range(n):\r\n    ls = input()\r\n    temp = ls.find(' ')\r\n    ls_1.append(int(ls[:temp]))\r\n    ls_2.append(int(ls[temp+1:]))\r\n\r\nfor i in range(n):\r\n    print(f(ls_1[i],ls_2[i]))"
  },
  "1868": {
    "sid": 2481679,
    "code": "Python",
    "content": "ls = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813,4817,4831,4861,4871,4877,4889,4903,4909,4919,4931,4933,4937,4943,4951,4957,4967,4969,4973,4987,4993,4999,5003,5009,5011,5021,5023,5039,5051,5059,5077,5081,5087,5099,5101,5107,5113,5119,5147,5153,5167,5171,5179,5189,5197,5209,5227,5231,5233,5237,5261,5273,5279,5281,5297,5303,5309,5323,5333,5347,5351,5381,5387,5393,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5591,5623,5639,5641,5647,5651,5653,5657,5659,5669,5683,5689,5693,5701,5711,5717,5737,5741,5743,5749,5779,5783,5791,5801,5807,5813,5821,5827,5839,5843,5849,5851,5857,5861,5867,5869,5879,5881,5897,5903,5923,5927,5939,5953,5981,5987,6007,6011,6029,6037,6043,6047,6053,6067,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6163,6173,6197,6199,6203,6211,6217,6221,6229,6247,6257,6263,6269,6271,6277,6287,6299,6301,6311,6317,6323,6329,6337,6343,6353,6359,6361,6367,6373,6379,6389,6397,6421,6427,6449,6451,6469,6473,6481,6491,6521,6529,6547,6551,6553,6563,6569,6571,6577,6581,6599,6607,6619,6637,6653,6659,6661,6673,6679,6689,6691,6701,6703,6709,6719,6733,6737,6761,6763,6779,6781,6791,6793,6803,6823,6827,6829,6833,6841,6857,6863,6869,6871,6883,6899,6907,6911,6917,6947,6949,6959,6961,6967,6971,6977,6983,6991,6997,7001,7013,7019,7027,7039,7043,7057,7069,7079,7103,7109,7121,7127,7129,7151,7159,7177,7187,7193,7207,7211,7213,7219,7229,7237,7243,7247,7253,7283,7297,7307,7309,7321,7331,7333,7349,7351,7369,7393,7411,7417,7433,7451,7457,7459,7477,7481,7487,7489,7499,7507,7517,7523,7529,7537,7541,7547,7549,7559,7561,7573,7577,7583,7589,7591,7603,7607,7621,7639,7643,7649,7669,7673,7681,7687,7691,7699,7703,7717,7723,7727,7741,7753,7757,7759,7789,7793,7817,7823,7829,7841,7853,7867,7873,7877,7879,7883,7901,7907,7919,7927,7933,7937,7949,7951,7963,7993,8009,8011,8017,8039,8053,8059,8069,8081,8087,8089,8093,8101,8111,8117,8123,8147,8161,8167,8171,8179,8191,8209,8219,8221,8231,8233,8237,8243,8263,8269,8273,8287,8291,8293,8297,8311,8317,8329,8353,8363,8369,8377,8387,8389,8419,8423,8429,8431,8443,8447,8461,8467,8501,8513,8521,8527,8537,8539,8543,8563,8573,8581,8597,8599,8609,8623,8627,8629,8641,8647,8663,8669,8677,8681,8689,8693,8699,8707,8713,8719,8731,8737,8741,8747,8753,8761,8779,8783,8803,8807,8819,8821,8831,8837,8839,8849,8861,8863,8867,8887,8893,8923,8929,8933,8941,8951,8963,8969,8971,8999,9001,9007,9011,9013,9029,9041,9043,9049,9059,9067,9091,9103,9109,9127,9133,9137,9151,9157,9161,9173,9181,9187,9199,9203,9209,9221,9227,9239,9241,9257,9277,9281,9283,9293,9311,9319,9323,9337,9341,9343,9349,9371,9377,9391,9397,9403,9413,9419,9421,9431,9433,9437,9439,9461,9463,9467,9473,9479,9491,9497,9511,9521,9533,9539,9547,9551,9587,9601,9613,9619,9623,9629,9631,9643,9649,9661,9677,9679,9689,9697,9719,9721,9733,9739,9743,9749,9767,9769,9781,9787,9791,9803,9811,9817,9829,9833,9839,9851,9857,9859,9871,9883,9887,9901,9907,9923,9929,9931,9941,9949,9967,9973]\r\na = int(input())\r\ni = 0\r\nsign = 0\r\nwhile i < a:\r\n    if ls[i]<a:\r\n        if sign!=9:\r\n            print(str(ls[i])+' ',end='')\r\n            sign += 1\r\n        else:\r\n            sign = 0\r\n            print(str(ls[i]))\r\n    i += 1\r\n"
  },
  "3031": {
    "sid": 2481678,
    "code": "Python",
    "content": "a = input()\r\ntemp = a.find(' ')\r\na_1 = a[:temp]\r\na_2 = a[temp+1:]\r\n\r\nc = int(a_1)+int(a_2)\r\nprint(\"a+b=\"+str(c),end='')"
  },
  "3088": {
    "sid": 2481677,
    "code": "Python",
    "content": "a = input()\r\nb = input()\r\nprint(a+b,end='')"
  },
  "3080": {
    "sid": 2481676,
    "code": "Python",
    "content": "a = input()\r\nsign = True\r\nfor i in range(len(a)):\r\n    if a[i] != a[len(a)-i-1]:\r\n        sign = False\r\n\r\nif sign:\r\n    print(1,end='')\r\nelse:\r\n    print(0,end='')"
  },
  "3769": {
    "sid": 2481675,
    "code": "Java",
    "content": "import java.util.ArrayList;\r\nimport java.util.List;\r\nimport java.util.Scanner;\r\n\r\nclass Main {\r\n\r\n    public static void main(String[] args){\r\n\r\n        Scanner scan = new Scanner(System.in);\r\n\r\n        int n = scan.nextInt();\r\n\r\n        List<Student> ls=new ArrayList<Student>();\r\n\r\n        for(int i = 0 ; i < n ; i++){\r\n\r\n            ls.add(new Student());\r\n            ls.get(i).student(scan.next(), scan.nextInt(), scan.nextInt(), scan.nextInt());\r\n\r\n        }\r\n\r\n        double x = 0,y = 0,z = 0;\r\n\r\n        for(int i = 0 ; i < n ; i++){\r\n\r\n            if(ls.get(i).getX()>=60){\r\n                x += 100;\r\n            }\r\n            if(ls.get(i).getY()>=60){\r\n                y += 100;\r\n            }\r\n            if(ls.get(i).getZ()>=60){\r\n                z += 100;\r\n            }\r\n\r\n        }\r\n\r\n        x /= n;\r\n        y /= n;\r\n        z /= n;\r\n\r\n        System.out.printf(\"%.2f %.2f %.2f\",x,y,z);\r\n\r\n    }\r\n}\r\n\r\nclass Student {\r\n\r\n    private String name;\r\n    private int x;\r\n    private int y;\r\n    private int z;\r\n\r\n    public void student(String student_name, int a, int b, int c){\r\n        name = student_name;\r\n        x = a;\r\n        y = b;\r\n        z = c;\r\n    }\r\n\r\n    public double get_num(){\r\n        return ((this.x+ this.y+ this.z)/3.0);\r\n    }\r\n\r\n    public String get_name(){\r\n        return  this.name;\r\n    }\r\n\r\n    public int getX(){\r\n        return this.x;\r\n    }\r\n\r\n    public int getY(){\r\n        return this.y;\r\n    }\r\n\r\n    public int getZ(){\r\n        return this.z;\r\n    }\r\n\r\n}\r\n"
  },
  "4212": {
    "sid": 2481674,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#define max(a,b) a>b?a:b\r\nusing namespace std;\r\nconst int MAXN(50000);\r\nint check[MAXN+50];\r\nint prime[MAXN];\r\nint a[MAXN+50];\r\nint haxi[MAXN+50];\r\nint len=0;\r\nvoid init() {\r\n    for(int i=2;i*i<=MAXN+50;i++) {\r\n        if(!check[i]) {\r\n            for(int j=i*i;j<MAXN+50;j+=i)\r\n                check[j]=1;\r\n        }\r\n    }\r\n    check[1]=1;\r\n    for(int i=2;i<=40000;i++) {\r\n        if(!check[i])\r\n            prime[len++]=i;\r\n    }\r\n}\r\nint main() {\r\n    init();\r\n    int n;\r\n    scanf(\"%d\",&n);\r\n    int ma=0,cnt=0;\r\n    for(int i=1;i<=n;i++) {\r\n        scanf(\"%d\",a+i);\r\n        haxi[a[i]]++;\r\n        ma=max(ma,a[i]);\r\n        if(a[i]==1)\r\n            cnt++;\r\n    }\r\n    int flag=0;\r\n    for(int i=1;i<=n;i++) {\r\n        if(a[i]==1) continue;\r\n        for(int j=0;j<len;j++) {\r\n            int temp=prime[j]-a[i];\r\n            if(temp>ma) break;\r\n            if(temp==a[i]&&haxi[temp]==1) continue;\r\n            if(haxi[temp]) {\r\n                flag=1;\r\n                break;\r\n            }\r\n        }\r\n        if(flag) break;\r\n    }\r\n    if(cnt>=2) {\r\n        for(int i=1;i<=n;i++) {\r\n            if(a[i]==1) continue;\r\n            if(!check[a[i]+1]) {\r\n                cnt++;\r\n                break;\r\n            }\r\n        }\r\n        cout<<cnt<<endl;\r\n    }\r\n    else if(!flag)\r\n        cout<<0<<endl;\r\n    else\r\n        cout<<2<<endl;\r\n}"
  },
  "3634": {
    "sid": 2481673,
    "code": "C",
    "content": "#include <stdio.h>\r\n\r\nint sum(int n){\r\n    int sum = 0, k = 1;\r\n    for (int i = 1; i <= n; i++){\r\n        for (int j = 1; j <= i; j++){\r\n            k *= j;\r\n        }\r\n        if (i % 2 == 0){\r\n            sum -= k;\r\n        }\r\n        else{\r\n            sum += k;\r\n        }\r\n        k = 1;\r\n    }\r\n    return sum;\r\n}\r\n\r\nint main() {\r\n    int n = 0;\r\n    scanf(\"%d\", &n);\r\n    printf(\"%d.00\", sum(n));\r\n    return 0;\r\n}"
  },
  "1016": {
    "sid": 2481672,
    "code": "C++",
    "content": "#include <iostream>\r\n#include<cstdio>\r\n/* run this program using the console pauser or add your own getch, system(\"pause\") or input loop */\r\nusing namespace std;\r\n\r\nint main(int argc, char** argv) {\r\n    int n;\r\n    double payment[1010];\r\n    char temp[1010];\r\n    while(cin>>n&&n){\r\n        double sum=0.0;\r\n        for(int i=0;i<n;i++){\r\n            cin>>payment[i];\r\n            sum+=payment[i];\r\n        }\r\n        double aver=((int)(sum*100))/n/100.0;\r\n        \r\n        sprintf(temp,\"%.2lf\",aver);\r\n        sscanf(temp,\"%lf\",&aver);\r\n        \r\n        double ans=0.0;\r\n        int count=0;\r\n        for(int i=0;i<n;i++){\r\n            if(payment[i]>aver+0.01){\r\n                ans+=(payment[i]-aver-0.01);\r\n                count++;\r\n            }\r\n        }\r\n        if(count*0.01>sum-aver*n)\r\n            ans+=(count*0.01-sum+aver*n);\r\n            \r\n        printf(\"$%.2lf\\n\",ans);\r\n        \r\n    }\r\n    return 0;\r\n}"
  },
  "5487": {
    "sid": 2481671,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n    printf(\"Hello World!\");\r\n}"
  },
  "5486": {
    "sid": 2481670,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n    printf(\"This is a C program.\");\r\n}"
  },
  "5485": {
    "sid": 2481669,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n    printf(\"******************************\\n\"\r\n           \"\\n\"\r\n           \"          Very good!\\n\"\r\n           \"\\n\"\r\n           \"******************************\");\r\n}"
  },
  "5484": {
    "sid": 2481668,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main(){\r\n    printf(\"*****\\n*\\n*\\n*\\n*****\");\r\n}"
  },
  "4800": {
    "sid": 2481667,
    "code": "C++",
    "content": "#include<iostream>\r\nusing namespace std;\r\ntypedef long long int ll;\r\nll pow(ll X,ll n)  //\u6b64\u9012\u5f52\u51fd\u6570\u529f\u80fd\u662f\u6c42X^a\u7684\u503c\r\n{\r\n    if(n==0)     //\u522b\u5fd8\u4e86\u5199\u9012\u5f52\u7ed3\u675f\u6761\u4ef6X^0=1\r\n       return 1;\r\n    ll m=n/2;       //b\u4e3aa\u7684\u6574\u96642\u7ed3\u679c\r\n    ll c=pow(X,m); //\u8fd9\u91cc\u7684c\u5c31\u76f8\u5f53\u4e8e\u516c\u5f0f\u4e2d\u7684X^b\r\n    c%=1003;    //\u4e0d\u65ad\u6c42\u4f59,\u9632\u6b62\u6ea2\u51fa\r\n    return n%2?c*c*X:c*c; //\u5957\u7528\u516c\u5f0f\u76f4\u63a5\u6c42\u51fa\u5e76\u8fd4\u56de\u6211\u4eec\u8981\u6c42\u7684X^a\u7684\u503c\r\n}\r\nint main()\r\n{\r\n    ll X,n;\r\n    cin>>X>>n;\r\n    cout<<(pow(X,n)%1003);\r\n    return 0;\r\n    //\u65f6\u95f4\u590d\u6742\u5ea6\u4e3aO(log2n)\r\n}\r\n"
  },
  "4801": {
    "sid": 2481666,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<stdio.h>\r\n\r\nusing namespace std;\r\n\r\n//\u6240\u6709\u5706\u76d8\u6309\u5927\u5c0f\u5347\u5e8f\u7f16\u53f7\r\n//n\u4e3a\u79fb\u52a8\u5706\u76d8\u603b\u6570\uff0cA\u4e3a\u8d77\u70b9\uff0cB\u4e3a\u4e2d\u8f6c\u7ad9\uff0cC\u4e3a\u7ec8\u70b9\r\nvoid Move(int n, char A, char B, char C)\r\n{\r\n\t//\u5206\u6790\u7684\u7ec8\u70b9\uff1a\u9876\u4e0a1\u4e2a\u5706\u76d8\u8be5\u4ece\u54ea\u79fb\u5230\u54ea\r\n\tif (n == 1) {\r\n\t\tprintf(\"Move disk %d from %c to %c\\n\", n, A, C);\r\n\t\treturn;\r\n\t}\r\n\t//\u8981\u60f3\u4eceA\u79fb\u52a8n\u4e2a\u5706\u76d8\u5230C\uff0c\u5e94\u5148\u5b9e\u73b0\u4eceA\u79fb\u52a8n-1\u4e2a\u5706\u76d8\u5230B\r\n\tMove(n - 1, A, C, B);\r\n\t//\u8fd9\u65f6A\u67f1\u53ea\u6709\u5706\u76d8n\uff0cC\u67f1\u4e3a\u7a7a\uff0c\u53ef\u4ee5\u76f4\u63a5\u5c06\u5706\u76d8n\u4eceA\u79fb\u5230C\r\n\tprintf(\"Move disk %d from %c to %c\\n\", n, A, C);\r\n\t//\u518d\u628aB\u67f1\u4e0a\u7684n-1\u4e2a\u5706\u76d8\u79fb\u5230C\u5373\u53ef\r\n\tMove(n - 1, B, A, C);\r\n}\r\n\r\nint main()\r\n{\r\n\tint N;//\u63a5\u6536\u8981\u79fb\u52a8\u5706\u76d8\u603b\u6570\r\n\tcin >> N;\r\n\t//\u5c06N\u4e2a\u5706\u76d8\u4eceA\u67f1\u79fb\u5230C\u67f1\uff0cB\u67f1\u4f5c\u4e3a\u4e2d\u8f6c\u7ad9\r\n\tMove(N, 'A', 'B', 'C');\r\n\treturn 0;\r\n}\r\n"
  },
  "4802": {
    "sid": 2481665,
    "code": "C++",
    "content": "#include <iostream>\r\n#include <string.h>\r\nusing namespace std;\r\n \r\nint main(int argc, char** argv) {\r\n    long long dp[55];\r\n    dp[1] = 1;\r\n    dp[2] = 2;\r\n    dp[3] = 3;\r\n    for(int i = 4; i <= 50; i++ ){\r\n    \tdp[i] = dp[i - 1] + dp[i - 2];\r\n\t}\r\n\tint n;\r\n\twhile(cin >> n){\r\n\t\tcout << dp[n] << endl;\r\n\t}\r\n    return 0;\r\n}\r\n"
  },
  "4850": {
    "sid": 2481664,
    "code": "C++",
    "content": "#include <cstdio>\r\n#include <algorithm>\r\nusing namespace std;\r\n\r\nconst int M = 2000010;\r\n\r\nint num[M];\r\n\r\n\r\n// \u8fd4\u56de\u6bcf\u7ec4\u4e2d\u4f4d\u6570\u4e2d\u7684\u4e2d\u4f4d\u6570\u7684\u6240\u5728\u4f4d\u7f6e\r\nint Quick_sort(int start, int end, int val) {\r\n\tint idx, left = start + 1, right = end;\r\n\tfor (int i = start; i <= end; ++i) {\r\n\t\tif (num[i] == val) {\r\n\t\t\tidx = i;\t\r\n\t\t\tswap(num[start], num[idx]);\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\twhile (left < right) {\r\n\t\twhile (num[left] < val && left < right) ++left;\r\n\t\twhile (num[right] > val && left < right) --right;\r\n\t\tif (left < right) swap(num[left], num[right]);\r\n\t}\r\n\tfor (int i = start; i <= end; ++i) {\r\n\t\tif (num[i] > num[start]) {\r\n\t\t\tswap(num[i - 1], num[start]);\r\n\t\t\treturn i - 1;\r\n\t\t}\r\n\t}\r\n}\r\n\r\n// \u8fd4\u56de[start, end]\u4e2d\u7b2ck\u5c0f\u7684\u6570\r\nint Solve(int start, int end, int k) {\r\n\tif (end - start < 75) {\r\n\t\tsort(num + start, num + end + 1);\r\n\t\treturn num[start + k - 1];\r\n\t}\r\n\tint cnt = 0;\r\n\t// \u6bcf5\u4e2a\u5143\u7d20\u5206\u4e3a1\u7ec4 \u8fdb\u884c\u6392\u5e8f\u540e \u5c06\u6bcf\u7ec4\u7684\u4e2d\u4f4d\u6570\u4f9d\u6b21\u4e0enum[start + cnt++]\u8fdb\u884c\u4e92\u6362 \u4e5f\u5c31\u662f\u672c\u6b21\u9012\u5f52\u4e2d\u7684\u5f00\u59cb\u53ca\u5f80\u540e\u7684\u4f4d\u7f6e\r\n\tfor (int i = start; i <= end; i += 5) {\r\n\t\tif (i + 4 <= end) {\r\n\t\t\tsort(num + i, num + i + 5);\r\n\t\t\tswap(num[start + cnt++], num[i + 2]);\r\n\t\t}\r\n\t\telse {\r\n\t\t\tsort(num + i, num + end + 1);\r\n\t\t\tswap(num[start + cnt++], num[(i + end + 1) >> 1]);\r\n\t\t}\r\n\t}\r\n\tint mid = Solve(start, start + cnt - 1, (cnt >> 1) + 1);\r\n\tint midd = Quick_sort(start, end, mid);\r\n\tint len = midd - start + 1;\r\n\t// \u5411\u5de6\u6216\u8005\u5411\u53f3\u9012\u5f52\r\n\tif (len >= k) return Solve(start, midd, k);\r\n\telse return Solve(midd + 1, end, k - len);\r\n}\r\n\r\nint main() {\r\n\tint n, k;\r\n\tscanf(\"%d%d\", &n, &k);\r\n\tfor (int i = 0; i < n; ++i) scanf(\"%d\", &num[i]);\r\n\tprintf(\"%d\", Solve(0, n - 1, k));\r\n\treturn 0;\r\n}\r\n"
  },
  "4892": {
    "sid": 2481663,
    "code": "C++",
    "content": "#include<bits/stdc++.h>\r\nusing namespace std;\r\n#define INF 999999999\r\nint n,m,edge[1001][1001],bj[1001],dp[1001];\r\nvoid djstl();\r\nint main()\r\n{\r\n    int i,j,a,b,c;\r\n    while(2==scanf(\"%d%d\",&n,&m))\r\n    {\r\n        memset(bj,false,sizeof(bj));\r\n        if(n==0&&m==0)\r\n        {\r\n            break;\r\n        }\r\n        for(i=1;i<=1000;i++)\r\n        {\r\n            dp[i]=INF;\r\n            for(j=1;j<=1000;j++)\r\n            {\r\n                edge[i][j]=INF;\r\n            }\r\n        }\r\n        dp[1]=0;\r\n        for(i=1;i<=m;i++)\r\n        {\r\n            scanf(\"%d%d%d\",&a,&b,&c);\r\n            edge[a][b]=min(c,edge[a][b]);\r\n            edge[b][a]=min(c,edge[b][a]);\r\n        }\r\n        djstl();\r\n        cout<<dp[n]<<endl;\r\n    }\r\n\r\n    return 0;\r\n}\r\nvoid djstl()\r\n{\r\n    int i,j,jh,zx;\r\n    for(i=1;i<=n;i++)\r\n    {\r\n        jh=-1;\r\n        zx=INF;\r\n        for(j=1;j<=n;j++)\r\n        {\r\n            if(!bj[j]&&dp[j]<zx)\r\n            {\r\n                jh=j;\r\n                zx=dp[j];\r\n            }\r\n        }\r\n        bj[jh]=true;\r\n        for(j=1;j<=n;j++)\r\n        {\r\n            if(!bj[j])\r\n            {\r\n                dp[j]=min(dp[j],dp[jh]+edge[jh][j]);\r\n            }\r\n        }\r\n    }\r\n}\r\n"
  },
  "4893": {
    "sid": 2481662,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#include<cmath>\r\n#include<cstring>\r\n#include<algorithm>\r\nusing namespace std;\r\n#define mem(a,b) memset(a,b,sizeof(a))\r\n#define MAXN 1000\r\n#define INF 9999999\r\n \r\nint cost[MAXN][MAXN];\r\nint mincost[MAXN];\r\nbool used[MAXN];\r\nint V,E;\r\n \r\nvoid prim(){\r\n\tfor(int i=1;i<=V;i++){\r\n\t\tmincost[i]=INF;\r\n\t\tused[i]=false;\r\n\t}\r\n\tmincost[1]=0;\r\n\tint res=0;\r\n\twhile(true){\r\n\t\tint v=-1;\r\n\t\tfor(int u=1;u<=V;u++){\r\n\t\t\tif(!used[u]&&(v==-1||mincost[u]<mincost[v]))\r\n\t\t\t\tv=u;\r\n\t\t}\r\n\t\tif(v==-1) break;\r\n\t\tused[v]=true;\r\n\t\tres+=mincost[v];\r\n\t\tfor(int u=1;u<=V;u++){\r\n\t\t\tmincost[u]=min(mincost[u],cost[v][u]);\r\n\t\t}\r\n\t}\r\n\tcout << res << endl;\r\n}\r\n \r\nint main(){\r\n\tios::sync_with_stdio(false);\r\n\twhile(cin >> V && V){\r\n\t\tint a,b,c,d;\r\n\t\tE=(V*(V-1))/2;\r\n\t\tfor(int i=1;i<=E;i++){\r\n\t\t\tcin >>a >> b >> c >> d;\r\n\t\t\tif(d==0){\r\n\t\t\t\tcost[a][b]=c;\r\n\t\t\t\tcost[b][a]=c;\r\n\t\t\t}else if(d==1){\r\n\t\t\t\tcost[a][b]=0;\r\n\t\t\t\tcost[b][a]=0;\r\n\t\t\t}\r\n\t\t}\r\n\t\tprim();\r\n\t}\r\n\treturn 0;\r\n}\r\n"
  },
  "4895": {
    "sid": 2481661,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#include<vector>\r\n#include<cstring>\r\n#include<stack>\r\n#include<queue>\r\n#include<map>\r\n#include<set> \r\n#include<algorithm>\r\nusing namespace std;\r\n#define lowbit(x) (x&-x)\r\n#define mem(a,b) memset(a,b,sizeof(a))\r\n#define eps 1e-9\r\n#define INF 999999\r\nconst int MAXN=105;\r\n \r\nint cost[MAXN][MAXN];\r\nint mincost[MAXN];\r\nbool used[MAXN];\r\nint V,E;\r\nint res=0;\r\nint prim(){\r\n\tmem(mincost,INF);\r\n\tmem(used,false);\r\n\t\r\n\tmincost[1]=0;\r\n\t\r\n\twhile(true){\r\n\t\tint v=-1;\r\n\t\t//\u4ece\u4e0d\u5c5e\u4e8eX\u7684\u9876\u70b9\u4e2d\u9009\u53d6\u4eceX\u5230\u5176\u6743\u503c\u6700\u5c0f\u7684\u9876\u70b9\r\n\t\tfor(int u=1;u<=V;u++){\r\n\t\t\tif(!used[u]&&(v==-1||mincost[u]<mincost[v]))\r\n\t\t\t\tv=u;\r\n\t\t} \r\n\t\tif(v==-1) break;\r\n\t\tused[v]=true;\r\n\t\tres+=mincost[v];\r\n\t\tfor(int u=1;u<=V;u++){\r\n\t\t\tmincost[u]=min(mincost[u],cost[v][u]);\r\n\t\t}\r\n\t}\r\n\treturn res;\r\n}\r\n \r\nint main(){\r\n\t\r\n\twhile(~scanf(\"%d\",&V) && V){\r\n\t\tmem(cost,0);\r\n\t\tres=0;\r\n\t\tE=V*(V-1)/2;\r\n\t\tint a,b,c;\r\n\t\tfor(int i=0;i<E;i++){\r\n\t\t\tscanf(\"%d%d%d\",&a,&b,&c);\r\n\t\t\tcost[a][b]=cost[b][a]=c;\r\n\t\t}\r\n\t\tprim();\r\n\t\tprintf(\"%d\\n\",res);\r\n\t}\r\n\t\r\n\treturn 0;\r\n}\r\n"
  },
  "4896": {
    "sid": 2481660,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\n#include<iostream>\r\nusing namespace std;\r\nint f[8005];\r\nint main(){\r\n\tint x,y,z,i,j,n;\r\n\tscanf(\"%d%d%d\",&x,&y,&z);\r\n\twhile(x||y||z){\r\n\t\tmemset(f,0,sizeof(f));\r\n\t\tf[0]=1;\r\n\t\tn=x+2*y+5*z;\r\n\t\tfor(i=1;i<=x;i<<=1){\r\n\t\t\tfor(j=n;j>=i;j--){\r\n\t\t\t\tf[j]|=f[j-i];\r\n\t\t\t}\r\n\t\t\tx-=i;\r\n\t\t}\r\n\t\tfor(j=n;j>=x;j--){\r\n\t\t\tf[j]|=f[j-x];\r\n\t\t}\r\n\t\tfor(i=1;i<=y;i<<=1){\r\n\t\t\tfor(j=n;j>=i*2;j--){\r\n\t\t\t\tf[j]|=f[j-i*2];\r\n\t\t\t}\r\n\t\t\ty-=i;\r\n\t\t}\r\n\t\tfor(j=n;j>=y*2;j--){\r\n\t\t\tf[j]|=f[j-y*2];\r\n\t\t}\r\n\t\tfor(i=1;i<=z;i<<=1){\r\n\t\t\tfor(j=n;j>=i*5;j--){\r\n\t\t\t\tf[j]|=f[j-i*5];\r\n\t\t\t}\r\n\t\t\tz-=i;\r\n\t\t}\r\n\t\tfor(j=n;j>=z;j--){\r\n\t\t\tf[j]|=f[j-z*5];\r\n\t\t}\r\n\t\tfor(i=0;f[i];i++);\r\n\t\tprintf(\"%d\\n\",i);\r\n\t\tscanf(\"%d%d%d\",&x,&y,&z);\r\n\t}\r\n\treturn 0;\r\n}\r\n"
  },
  "4898": {
    "sid": 2481659,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#include<cstdlib>\r\n#include<string>\r\n#include<cstring>\r\n#include<cmath>\r\n#include<ctime>\r\n#include<algorithm>\r\n#include<utility>\r\n#include<stack>\r\n#include<queue>\r\n#include<vector>\r\n#include<set>\r\n#include<map>\r\n#define EPS 1e-9\r\n#define PI acos(-1.0)\r\n#define INF 0x3f3f3f3f\r\n#define LL long long\r\nconst int MOD = 1E9+7;\r\nconst int N = 10000+5;\r\nconst int dx[] = {0,0,-1,1,-1,-1,1,1};\r\nconst int dy[] = {-1,1,0,0,-1,1,-1,1};\r\nusing namespace std;\r\n \r\nint a[N];//\u6743\u91cd\u4e3ai\u7684\u7ec4\u5408\u6570\r\nint b[N];//\u4e34\u65f6\u6570\u7ec4\r\nint P;//\u6700\u5927\u6307\u6570\r\nint v[N],n1[N],n2[N];\r\nvoid cal(int k){\r\n    memset(a,0,sizeof(a));\r\n    a[0]=1;\r\n    for(int i=1;i<=k;i++){//\u5faa\u73af\u6bcf\u4e2a\u56e0\u5b50\r\n        memset(b,0,sizeof(b));\r\n        for(int j=n1[i];j*v[i]<=P;j++)//\u5faa\u73af\u6bcf\u4e2a\u56e0\u5b50\u7684\u6bcf\u4e00\u9879\uff0cn2\u662f\u65e0\u7a77\uff0c\u53bb\u6389\u539f\u6709\u7684j<=n2[i]\r\n            for(int k=0;k+j*v[i]<=P;k++)//\u5faa\u73afa\u7684\u6bcf\u4e2a\u9879\r\n                b[k+j*v[i]]+=a[k];//\u628a\u7ed3\u679c\u52a0\u5230\u5bf9\u5e94\u4f4d\r\n        memcpy(a,b,sizeof(b));//b\u8d4b\u503c\u7ed9a\r\n    }\r\n}\r\nint main(){\r\n    for(int i=1;i<=17;i++)\r\n        v[i]=i*i;\r\n    int n;\r\n    while(scanf(\"%d\",&n)!=EOF&&n){\r\n        memset(n1,0,sizeof(n1));\r\n        P=n;\r\n        cal(17);\r\n        printf(\"%d\\n\",a[P]);\r\n    }\r\n    return 0;\r\n}\r\n"
  },
  "1847": {
    "sid": 2480984,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint x,y,a,b;\r\n\tscanf(\"%d%d\",&x,&y);\r\n\ta=y;\r\n\tb=x;\r\n\tx=a;\r\n\ty=b;\r\n\tprintf(\"%d %d\",x,y);\r\n} "
  },
  "1848": {
    "sid": 2480983,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a,b;\r\n\ta=getchar();\r\n\tb=a-32;\r\n    putchar(b);\r\n}"
  },
  "1882": {
    "sid": 2480982,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint x,y,a;\r\n\tscanf(\"%d\\\\%d\",&x,&y);\r\n\tif(y==1||y==3||y==5||y==7||y==8||y==10||y==12)\r\n\ta=31;\r\n\tif(y==4||y==6||y==9||y==11)\r\n\ta=30;\r\n\tif(y==2)\r\n\t{\r\n\t\tif(x%4==0&&x%100!=0||x%400==0)\r\n\t\ta=29;\r\n\t\telse \r\n\t\ta=28;\r\n\t}\r\n\tprintf(\"%d\",a);\r\n}"
  },
  "1864": {
    "sid": 2480981,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,d;\r\n\tchar c;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tgetchar();\r\n\tc=getchar();\r\n\tswitch(c)\r\n\t{\r\n\tcase'+':d=a+b;break;\r\n\tcase'-':d=a-b;break;\r\n\tcase'*':d=a*b;break;\r\n\tcase'/':d=a/b;\r\n\t}\r\n\tprintf(\"%d\",d);\r\n} "
  },
  "1508": {
    "sid": 2480980,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,i,j,m,n,x;\r\n    scanf(\"%d\",&a);\r\n\ti=a/10000;\r\n\tj=(a%10000)/1000;\r\n\tm=((a%10000)%1000)/100;\r\n\tn=(((a%10000)%1000)%100)/10;\r\n\tx=a%10;\r\n\tif(a>=0&&a<100000)\r\n\t{\r\n\tif(i!=0)\r\n\tprintf(\"5\\n%d %d %d %d %d\\n%d%d%d%d%d\",i,j,m,n,x,x,n,m,j,i);\r\n\telse if(j!=0)\r\n\tprintf(\"4\\n%d %d %d %d\\n%d%d%d%d\",j,m,n,x,x,n,m,j);\r\n\telse if(m!=0)\r\n\tprintf(\"3\\n%d %d %d\\n%d%d%d\",m,n,x,x,n,m);\r\n\telse if(n!=0)\r\n\tprintf(\"2\\n%d %d\\n%d%d\",n,x,x,n);\r\n\telse\r\n\tprintf(\"1\\n%d\\n%d\",x,x);\r\n\t}\r\n}"
  },
  "1509": {
    "sid": 2480979,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a,b;\r\n\tscanf(\"%f\",&a);\r\n\tif(a>=0)\r\n\t{\r\n\tif(a<=100000)\r\n\tb=a*0.1;\r\n\telse if(a<=200000)\r\n\tb=(a-100000)*0.075+100000*0.1;\r\n\telse if(a<=400000)\r\n\tb=(a-200000)*0.05+100000*0.075+100000*0.1;\r\n\telse if(a<=600000)\r\n\tb=(a-400000)*0.03+200000*0.05+100000*0.075+100000*0.1;\r\n\telse if(a<=1000000)\r\n\tb=(a-600000)*0.015+200000*0.03+200000*0.05+100000*0.075+100000*0.1;\r\n\telse\r\n\tb=(a-1000000)*0.01+400000*0.015+200000*0.03+200000*0.05+100000*0.075+100000*0.1;\r\n\t}\r\n\tprintf(\"%.0f\",b);\r\n}"
  },
  "1843": {
    "sid": 2480978,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"100\\nA\\n3.140000\\n\");\r\n} "
  },
  "1889": {
    "sid": 2480977,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a,i,j,m,n,f;\r\n\tscanf(\"%f%f%f\",&a,&i,&j);\r\n\tm=a+i+j;\r\n\tn=a*i*j;\r\n\tf=m/3;\r\n\tprintf(\"%.0f %.0f %.2f\",m,n,f);\r\n}"
  },
  "3605": {
    "sid": 2480976,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d\",&a);\r\n    b=2*a+1;\r\n    printf(\"%d\",b);\r\n}"
  },
  "3609": {
    "sid": 2480975,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,temp,x;\r\n\tscanf(\"%d,%d,%d\",&a,&b,&c);\r\n    temp=b;\r\n    b=a;\r\n    x=c;\r\n    c=temp;\r\n    a=x;\r\n    printf(\"%d,%d,%d\",a,b,c);\r\n}"
  },
  "1851": {
    "sid": 2480973,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tswitch(a)\r\n\t{\r\n\t\tcase 1:printf(\"Monday\");break;\r\n\t\tcase 2:printf(\"Tuesday\");break;\r\n\t\tcase 3:printf(\"Wednesday \");break;\r\n\t\tcase 4:printf(\"Thursday\");break;\r\n\t\tcase 5:printf(\"Friday\");break;\r\n\t\tcase 6:printf(\"Saturday\");break;\r\n\t\tcase 7:printf(\"Sunday\");\r\n\t}\r\n} "
  },
  "1912": {
    "sid": 2480972,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,max,min,m;\r\n\tscanf(\"%d %d %d\",&a,&b,&c);\r\n\tmax=(a>b)?a:b;\r\n\tmax=(c>max)?c:max;\r\n\tmin=(a>b)?b:a;\r\n\tmin=(min>c)?c:min;\r\n\tm=a+b+c-min-max;\r\n\tprintf(\"%d\",m);\r\n}"
  },
  "1924": {
    "sid": 2480971,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n    if(a%5==0&&a%3==0)\r\n    printf(\"Yes\");\r\n    else\r\n\tprintf(\"No\");\t\r\n} "
  },
  "1928": {
    "sid": 2480970,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat a,b,c,p,x,s;\r\n\tscanf(\"%f%f%f\",&a,&b,&c);\r\n    p=(a+b+c)/2;\r\n    x=p*(p-a)*(p-b)*(p-c);\r\n    s=sqrt(x);\r\n\tprintf(\"%.3f\",s);\t\r\n}"
  },
  "1929": {
    "sid": 2480969,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat r,h,c,s,s1,v,pai;\r\n\tpai=3.1415926;\r\n\tscanf(\"%f %f\",&r,&h);\r\n\tc=2*pai*r;\r\n\ts=pai*r*r;\r\n\ts1=c*h;\r\n\tv=s*h;\r\n\tprintf(\"%.2f %.2f %.2f %.2f\",c,s,s1,v);\r\n}\r\n"
  },
  "3072": {
    "sid": 2480968,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,c,y,m,n;\r\n\tchar b;\r\n\tscanf(\"%d%c%d\",&a,&b,&c);\r\n\t       if(a>0)\r\n\t\t\tm=a;\r\n\t\t\telse\r\n\t\t\tm=-a;\r\n\t\t\tif(c>0)\r\n\t\t\tn=c;\r\n\t\t\telse\r\n\t\t\tn=-c;\r\n\tswitch(b)\r\n\t{\r\n\t\tcase'#':y=a*a+c*c;break;\r\n\t\tcase'$':y=m+n;break;\r\n\t\tcase'%':y=a%c;\r\n\t}\r\n\tprintf(\"%d\",y);\r\n} "
  },
  "3098": {
    "sid": 2480966,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat a,b,c,d,x,x1,m,n;\r\n\tscanf(\"%f%f%f\",&a,&b,&c);\r\n\tif(a!=0)\r\n\t{\r\n\t\td=b*b-4*a*c;\r\n\t\tif(d<0)\r\n\t    printf(\"\u65e0\u6839\");\r\n\t    else if(d==0)\r\n\t    {\r\n\t    x=(-b)/2*a;\r\n\t    printf(\"%.2f\",x);\r\n\t    }\r\n\t    else\r\n\t    {\r\n\t    x=((-b)+sqrt(d))/2*a;\r\n\t\tx1=((-b)-sqrt(d))/2*a;\r\n\t\tm=(x>x1)?x:x1;\r\n\t\tn=(x>x1)?x1:x;\r\n\t\tprintf(\"%.2f %.2f\",m,n);\r\n\t    }\r\n\t} \r\n\telse\r\n\tprintf(\"\u4e0d\u662f\u4e00\u5143\u4e8c\u6b21\u65b9\u7a0b\");\r\n} "
  },
  "1814": {
    "sid": 2480964,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n=0;\r\n\tscanf(\"%d-%d-%d\",&i,&j,&m);\r\n\tswitch(j)\r\n\t{\r\n\t\tcase 12:n+=30;\r\n\t\tcase 11:n+=31;\r\n\t\tcase 10:n+=30;\r\n\t\tcase 9:n+=31;\r\n\t\tcase 8:n+=31;\r\n\t\tcase 7:n+=30;\r\n\t\tcase 6:n+=31;\r\n\t\tcase 5:n+=30;\r\n\t\tcase 4:n+=31;\r\n\t\tcase 3:n+=28;\r\n\t\tcase 2:n+=31;\r\n\t\tcase 1:n+=m;\r\n\t}\r\n\tif((i%4==0&&i%100!=0||i%400)&&j>=3)\r\n\tn++;\r\n\tprintf(\"%d\",n);\r\n}"
  },
  "1853": {
    "sid": 2480963,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,k,a,b,c;\r\n\tfor(a=1;a<4;a++)\r\n\t{\r\n\t\tfor(b=1;b<=(4-a);b++)\r\n\t\tprintf(\" \");\r\n\t\tfor(c=1;c<=1+2*(a-1);c++)\r\n\t\tprintf(\"*\");\r\n\t\tprintf(\"\\n\"); \r\n\t}\r\n\tfor(i=0;i<4;i++)\r\n\t{\r\n\t\tfor(k=1;k<=i;k++)\r\n\t\tprintf(\" \");\r\n\t\tfor(j=0;j<7-i*2;j++)\r\n\t\tprintf(\"*\");\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\t\r\n}"
  },
  "1854": {
    "sid": 2480962,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,i,j,m,n;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=2;i<=((a+1)/2);i++)\r\n\t{\r\n\t\tj=a%i;\r\n\t\tif(j==0)\r\n\t\t{\r\n\t\t\tprintf(\"This is not a prime.\");\r\n            break;\r\n\t\t}\r\n\t\tif(i==((a+1)/2))\r\n\t\tprintf(\"This is a prime.\");\r\n\t}\r\n}"
  },
  "1870": {
    "sid": 2480961,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,i,j,m,n,n1;\r\n\tscanf(\"%d%d%d\",&a,&b,&c);\r\n\ti=a+b;\r\n\tj=a+c;\r\n\tm=b+c;\r\n\tn=(i>j)?i:j;\r\n\tn1=(n>m)?n:m;\r\n\tprintf(\"%d\",n1);\r\n}"
  },
  "1892": {
    "sid": 2480960,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i=0,j=0;\r\n\tchar m,str[100];\r\n\twhile(~(m=getchar())&&m!='\\n')\r\n\t{\r\n\t\tstr[i]=m;\r\n\t\ti++;\r\n\t}\r\n\tfor(j=i-1;j>=0;j--)\r\n\tprintf(\"%c\",str[j]);\r\n}"
  },
  "3629": {
    "sid": 2480958,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a;\r\n\tint b,c;\r\n\tscanf(\"%c\",&a);\r\n\tb=a;\r\n\tif(b>=48&&b<=57)\r\n\tc=3;\r\n\telse if(b>=65&&b<=90)\r\n\tc=1;\r\n\telse if(b>=97&&b<=122)\r\n\tc=2;\r\n\telse\r\n\tc=4;\r\n\tprintf(\"%d\",c);\r\n\t\r\n} "
  },
  "3058": {
    "sid": 2480956,
    "code": "C++",
    "content": "\n#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,d,e,f,x,y;\r\n\tscanf(\"%d:%d:%d\",&a,&b,&c);\r\n\td=c+1;\r\n\te=b+1;\r\n\tf=a+1;\r\n\tx=0;\r\n\ty=0;\r\n\tif(d==60&&e!=60)\r\n\t{\r\n\t\tprintf(\"%d:%d:%d\",a,e,x);\r\n\t}\r\n\telse if(d==60&&e==60)\r\n\t{\r\n\t\tprintf(\"%d:%d:%d\",f,y,x);\r\n\t}\r\n\telse\r\n\t{\r\n\t\tprintf(\"%d:%d:%d\",a,b,d);\r\n\t}\r\n \r\n} "
  },
  "3625": {
    "sid": 2480955,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,m,n;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tif(a<0)\r\n\tm=-a;\r\n\tif(b<0)\r\n\tn=-b;\r\n\tif(m>n)\r\n\tprintf(\"%d\",a);\r\n\telse\r\n\tprintf(\"%d\",b);\r\n}"
  },
  "3630": {
    "sid": 2480953,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint x,y,i,j,a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tfor(i=1;i<=a;i++)\r\n\t{\r\n\t\tx=i;\r\n\t\ty=a-i;\r\n\t\tif((x*2+y*4)==b)\r\n\t\tprintf(\"%d %d\",x,y);\r\n\t}\r\n}"
  },
  "3631": {
    "sid": 2480952,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint y,a,i,j,m,n;\r\n\tfor(a=1000;a<10000;a++)\r\n\t{\r\n\t\ti=a/1000;\r\n\t    j=(a%1000)/100;\r\n    \tm=((a%1000)%100)/10;\r\n    \tn=a%10;\r\n    \ty=((i*10+j)+(m*10+n))*((i*10+j)+(m*10+n));\r\n\t\tif(y==a)\r\n\t\tprintf(\"%d\\n\",a);\r\n\t}\r\n}"
  },
  "3803": {
    "sid": 2480946,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j=1,m=0,f=0,sum=0,a;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=0;i<a;i++)\r\n\t{\t\r\n\t    m=f;\r\n\t    f=m+j;\r\n\t\tj=m;\r\n\t\tif(i<a-1)\r\n\t\tprintf(\"%d,\",f);\r\n\t\telse\r\n\t\tprintf(\"%d\",f);\r\n\t}\r\n}"
  },
  "3804": {
    "sid": 2480944,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,i,j,m,n[32];\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=0;i<=32&&a!=0;i++)\r\n\t{\r\n\t\tn[i]=a%2;\r\n\t\ta=a/2;\r\n\t}\r\n\tfor(i=i-1;i>=0;i--)\r\n\t{\r\n\t\tprintf(\"%d\",n[i]);\r\n\t}\r\n\t\r\n}"
  },
  "3637": {
    "sid": 2480943,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a;\r\n\tint b;\r\n\tscanf(\"%c\",&a);\r\n    b=a;\r\n    if(a>='a'&&a<='z'||a>='A'&&a<='Z')\r\n    printf(\"%d\",b);\r\n    else if(a>='0'&&a<='9')\r\n\tprintf(\"%c\",a);\r\n\telse\r\n\tprintf(\"wrong character!\");\r\n}"
  },
  "3888": {
    "sid": 2480942,
    "code": "C++",
    "content": "#include<stdio.h>\r\nvoid f1(int a,int b,int *t)\r\n{\r\n\t*t=a+b;\r\n}\r\nint main()\r\n{\r\n\tint a,b,t;\r\n\tscanf(\"%d,%d\",&a,&b);\r\n\tf1(a,b,&t);\r\n\tprintf(\"%d\",t);\r\n}"
  },
  "3827": {
    "sid": 2480940,
    "code": "C++",
    "content": "#include <stdio.h>\r\n#define AREA(x,y) x*y\r\n\r\nint main()\r\n\r\n{\r\n\r\nint a,b;\r\n\r\nscanf(\"%d,%d\",&a,&b);\r\n\r\nprintf(\"%d\",AREA((a+2),(b+3)));\r\n\r\nreturn 0;\r\n\r\n}"
  },
  "3867": {
    "sid": 2480936,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tfloat i,j,m,n,a,c;\r\n\tint b;\r\n\tfor(b=1000;b<10000;b++)\r\n\t{\r\n\t\ti=b/1000;\r\n\t\tj=((b%1000))/100;\r\n\t\tm=((b%1000)%100)/10;\r\n\t\tn=b%10;\r\n\t\tc=sqrt(b);\r\n\t\tif(i==j&&m==n&&c==(int)c)\r\n\t\t{\r\n\t\tprintf(\"%d\",b);\r\n\t\tbreak;\r\n\t\t}\r\n\t} \r\n}"
  },
  "3820": {
    "sid": 2480935,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tscanf(\"%d,%d\",&a,&b);\r\n\tc=a*b;\r\n\tprintf(\"%d\",c);\r\n}"
  },
  "3633": {
    "sid": 2480934,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a,b,c,y,a1,b1,c1;\r\n\tfor(a=0;a<=100;a++)\r\n\t{\r\n\t\tfor(b=0;b<=100;b++)\r\n\t\t{\r\n\t\t\tfor(c=0;c<=100;c++)\r\n\t\t\t{\r\n\t\t\t\ta1=5*a;\r\n\t\t\t    b1=b*3;\r\n\t\t\t    c1=c/3;\r\n\t\t\t    y=a1+b1+c1;\r\n\t\t\t    if(y==100&&(a+b+c)==100)\r\n\t\t\t    printf(\"%.0f %.0f %.0f\\n\",a,b,c);\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
  },
  "3647": {
    "sid": 2480932,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    int a,b,c,i,j;\r\n    scanf(\"%d,%d,%d\",&a,&b,&c);\r\n    i=a>b?a:b;\r\n    i=i>c?i:c;\r\n    j=a>b?b:a;\r\n    j=j>c?c:j;\r\n    printf(\"%d,%d\",i,j);\r\n}\r\n"
  },
  "1832": {
    "sid": 2480931,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n   int n,m,a[100],i,t,j,m1,n1;\r\n   while(scanf(\"%d %d\",&n,&m)&&n||m)\r\n   {\r\n        for(i=0;i<n;i++)\r\n        scanf(\"%d\",&a[i]);\r\n        a[n]=m;\r\n        for(i=0;i<=n;i++)\r\n        {\r\n            for(j=i+1;j<=n;j++)\r\n            {\r\n                if(a[i]>a[j])\r\n                {\r\n                   t=a[i];\r\n                   a[i]=a[j];\r\n                   a[j]=t;\r\n                }\r\n            }\r\n        }\r\n        for(i=0;i<=n;i++)\r\n        {\r\n            if(i==n)\r\n            printf(\"%d\\n\",a[n]);\r\n            else\r\n            printf(\"%d \",a[i]);\r\n        }\r\n   }\r\n     return 0;\r\n}"
  },
  "1828": {
    "sid": 2480930,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat m,j=1,a,c=0,b,i;\r\n    while(~(scanf(\"%f\",&m)))\r\n\t{\r\n\t\tfor(a=0;a<m;a++)\r\n\t\t{\r\n\t\t\tscanf(\"%f\",&b);\r\n\t\t\tc=0;\r\n\t\t\tj=1;\r\n\t\t\tfor(i=1;i<=b;i++)\r\n        \t{\r\n        \t\tj=1/i;\r\n        \t\tif((int)i%2==0)\r\n \t            j=-j;\r\n\t        \tc=c+j;\r\n        \t}\r\n        \tprintf(\"%.2f\\n\",c);\r\n\t\t}\r\n\t}\r\n\t\r\n}"
  },
  "1825": {
    "sid": 2480928,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat n;\r\n\twhile(~(scanf(\"%f\",&n)))\r\n\t{\r\n\t\tif(n>=0)\r\n\t\tn=n;\r\n\t\tif(n<0)\r\n\t\tn=-n;\r\n\t\tprintf(\"%.2f\\n\",n);\r\n\t}\r\n}"
  },
  "1827": {
    "sid": 2480927,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\n#include<math.h>\r\ndouble jisuan(int n,int m)\r\n{\r\n    double a=n,i,z;\r\n    z=a;\r\n    for(i = 2; i <= m; i++)\r\n    {\r\n        a =sqrt(a);\r\n        z=z+a;\r\n    }\r\n    return z;\r\n}\r\n\r\nint main()\r\n{\r\n    int n,m;\r\n    while(~scanf(\"%d %d\",&n,&m))\r\n    {\r\n        printf(\"%.2lf\\n\",jisuan(n,m));\r\n    }\r\n    return 0;\r\n}\r\n"
  },
  "3741": {
    "sid": 2480926,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,a,b[5]={0};\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=4;i>=0;i--)\r\n\t{\r\n\t\tb[i]=a%2;\r\n\t\ta=a/2;\r\n\t\tif(a==0)\r\n\t\tbreak;\r\n\t}\r\n\tfor(j=0;j<5;j++)\r\n\t{\r\n\t\tprintf(\"%d\",b[j]);\r\n\t}\r\n} "
  },
  "3778": {
    "sid": 2480925,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a,b,c;\r\n\twhile(~(scanf(\"%f %f\",&a,&b)))\r\n\t{\r\n\t\tc=a+b;\r\n\t\tprintf(\"%.2f\\n\",c);\r\n\t}\r\n}"
  },
  "3092": {
    "sid": 2480922,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100][100];\r\n\tint n,m,i,j;\r\n\tscanf(\"%d\",&n);\r\n\tm=getchar();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<100&&a[i][j]!='\\0';j++)\r\n\t\t{\r\n\t\t\tm=a[i][j];\r\n\t\t\tif(m<='0'||m>='9')\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%c\",a[i][j]);\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "3259": {
    "sid": 2480921,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j=0,a[10];\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t\tj=j+a[i];\r\n\t}\r\n\tprintf(\"%d\",j);\r\n\t\r\n}"
  },
  "1537": {
    "sid": 2480920,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\n#define p(a,b,c) (a+b+c)/2\r\n#define area(a,b,c,p) sqrt(p*(p-a)*(p-b)*(p-c))\r\nint main()\r\n{\r\n\tfloat a,b,c,d;\r\n\tscanf(\"%f%f%f\",&a,&b,&c);\r\n    d=area(a,b,c,p(a,b,c));\r\n\tprintf(\"%.3f\",d);\r\n}"
  },
  "1830": {
    "sid": 2480919,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n  int m,n,i,line[104],s,j,h;\r\n  int aver1,aver2;\r\n  while(scanf(\"%d%d\",&n,&m)!=EOF)\r\n  {\r\n     line[0]=2;\r\n     for(i=1;i<n;i++)\r\n     line[i]=line[i-1]+2;\r\n     h=n%m;\r\n     for(j=0;j<n/m;j++)\r\n     {\r\n         s=0;\r\n         for(i=j*m;i<(j+1)*m;i++)\r\n         s=line[i]+s;\r\n         aver1=s/m;\r\n         if(j==0)\r\n         printf(\"%d\",aver1);\r\n         else printf(\" %d\",aver1);\r\n      } \r\n      if(h!=0)\r\n      {\r\n        s=0;\r\n        for(i=n-h;i<n;i++)\r\n        s=s+line[i];\r\n        aver2=s/h;\r\n        if(n/m==0)\r\n        printf(\"%d\",aver2);\r\n        else\r\n        printf(\" %d\",aver2);\r\n      }\r\n      printf(\"\\n\");\r\n  } \r\n  return 0;\r\n}"
  },
  "1910": {
    "sid": 2480918,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    int n;\r\n    while(~scanf(\"%d\",&n)&&n!=0)\r\n    {\r\n    \tint t,t1,y,i,j,x,m=0;\r\n    \tint a[100],b[100];\r\n    \tfor(i=0;i<n;i++)\r\n    \t{\r\n\t    \tscanf(\"%d\",&a[i]);\r\n\t    }\r\n\t    for(i=0;i<n;i++)\r\n\t    {\r\n\t    \tm=0;\r\n\t    \ty=a[i];\r\n    \t   while(y!=0)\r\n    \t   {\r\n    \t   \tj=y%10;\r\n    \t   \tm=m+j;\r\n    \t   \ty=y/10;\t\t     \t\r\n   \t       }\r\n   \t       b[i]=m;\r\n    \t}\r\n    \tfor(i=0;i<n-1;i++)\r\n    \t{\r\n\t    \tfor(x=0;x<n-1-i;x++)\r\n\t    \t{\r\n\t    \t\tif(b[x]>b[x+1])\r\n\t    \t\t{\r\n\t\t    \t\tt=a[x];\r\n\t\t    \t\ta[x]=a[x+1];\r\n\t\t    \t\ta[x+1]=t;\r\n\t\t    \t\tt1=b[x];\r\n\t\t    \t\tb[x]=b[x+1];\r\n\t\t    \t\tb[x+1]=t1;\r\n\t\t    \t}\r\n\t    \t}\r\n\t    }\r\n\t    for(i=0;i<n;i++)\r\n\t    {\r\n\t    \tif(i<n-1)\r\n    \t\tprintf(\"%d \",a[i]);\r\n    \t\telse\r\n\t\t\tprintf(\"%d\\n\",a[i]);\r\n    \t}\r\n    }\r\n}\r\n"
  },
  "1901": {
    "sid": 2480917,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,x,y;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tfor(j=n-i;j>=1;j--)\r\n\t\t{\r\n\t\t\tprintf(\" \");\r\n\t\t}\r\n\t\tfor(m=1;m<=i;m++)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",m);\r\n\t\t}\r\n\t\tfor(x=i-1;x>0;x--)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",x);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\tfor(i=n-1;i>=1;i--)\r\n\t{\r\n\t\tfor(j=1;j<=n-i;j++)\r\n\t\t{\r\n\t\t\tprintf(\" \");\r\n\t\t}\r\n\t\tfor(m=1;m<=i;m++)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",m);\r\n\t\t}\r\n\t\tfor(x=i-1;x>0;x--)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",x);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1925": {
    "sid": 2480916,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i,j;\r\n\tscanf(\"%d\",&n);\r\n\tn=n*10;\r\n\ti=n/3;\r\n\tj=n%3;\r\n\tprintf(\"%d %d\",i,j);\r\n}"
  },
  "1931": {
    "sid": 2480915,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat n;\r\n\twhile((scanf(\"%f\",&n))!=EOF)\r\n\t{\r\n\t\tif(n<0)\r\n\t\tn=-n;\r\n\t\telse\r\n\t\tn=n;\r\n\t\tprintf(\"%.2f\\n\",n);\r\n\t}\r\n}"
  },
  "1902": {
    "sid": 2480914,
    "code": "C",
    "content": "#include <stdio.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tint s=0,i;\r\n\tgets(a);\r\n\tif(a[0]!=' ')\r\n\t{\r\n\t\ts=1;\r\n\t}\r\n\tfor(i=1;a[i]!='\\0';i++)\r\n\t{\r\n\t\tif(a[i-1]==' '&&a[i]!=' ')\r\n\t\t{\r\n\t\t\ts++;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",s);\r\n}\r\n"
  },
  "1904": {
    "sid": 2480913,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint s=0,i,n,a,b,c,d;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ts=0;\r\n\t\tscanf(\"%d %d %d\",&a,&b,&c);\r\n\t\tswitch(b)\r\n\t\t{\r\n\t\t\tcase 12:s=s+30;\r\n\t\t\tcase 11:s=s+31;\r\n\t\t\tcase 10:s=s+30;\r\n\t\t\tcase 9:s=s+31;\r\n\t\t\tcase 8:s=s+31;\r\n\t\t\tcase 7:s=s+30;\r\n\t\t\tcase 6:s=s+31;\r\n\t\t\tcase 5:s=s+30;\r\n\t\t\tcase 4:s=s+31;\r\n\t\t\tcase 3:s=s+28;\r\n\t\t\tcase 2:s=s+31;\r\n\t\t\tcase 1:s=s+c;\r\n\t\t}\r\n\t\tif((a%4==0&&a%100!=0||a%400==0)&&b>=3)\r\n    \ts=s+1;\r\n    \tprintf(\"%d\\n\",s);\r\n\t}\r\n}"
  },
  "1926": {
    "sid": 2480912,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tint i,j,m,n;\r\n\tfor(i=0;a[i]!='\\0';i++)\r\n\t{\r\n\t\ta[i]=a[i]+4;\r\n\t}\r\n\tprintf(\"password is \");\r\n\tputs(a);\r\n}"
  },
  "1916": {
    "sid": 2480911,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n   int n,i,j;\r\n   double x,s,a;\r\n   while(scanf(\"%lf %d\",&x,&n)!=EOF)\r\n   {\r\n      s=1;\r\n      for(i=1;i<=n;i++)\r\n      {\r\n          a=1;\r\n          for(j=1;j<=2*i;j++)\r\n          {\r\n             a=a*j;\r\n          }\r\n             s=s+pow(-1,i)*pow(x,2*i)/a;\r\n      }\r\n      printf(\"%.4lf\\n\",s);\r\n   }\r\n   return 0;\r\n}\r\n"
  },
  "1908": {
    "sid": 2480909,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100],b[100],i,j,m,n;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=n-m,j=0;i<n;i++,j++)\r\n\t{\r\n\t\tb[j]=a[i];\r\n\t}\r\n\tfor(i=0;i<n-m;i++,j++)\r\n\t{\r\n\t\tb[j]=a[i];\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(i==n-1)\r\n\t\tprintf(\"%d\",b[i]);\r\n\t\telse\r\n\t\tprintf(\"%d \",b[i]);\r\n\t}\r\n}"
  },
  "1906": {
    "sid": 2480908,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,n;\r\n\tfloat a,b,c,d,h,sum;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tsum=0;\r\n\t\tscanf(\"%f%f\",&a,&b);\r\n\t\th=a;\r\n\t\tfor(j=0;j<b;j++)\r\n\t\t{\r\n\t\t\tif(j==0)\r\n\t\t\tsum=sum+h;\r\n\t\t\telse\r\n\t\t\tsum=sum+2*h;\r\n            h=h/2;\r\n\t\t}\r\n\t\tprintf(\"%.2f %.2f\\n\",sum,h);\r\n\t}\r\n}"
  },
  "1913": {
    "sid": 2480907,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i=0,j=0,m,m1,a[5],n,b[5],c;\r\n\tscanf(\"%d\",&n);\r\n\tm=n;\r\n\twhile(m!=0)\r\n\t{\r\n\t\tm1=m%10;\r\n\t\ta[i]=m1;\r\n\t\tm=m/10;\r\n\t\tj++;\r\n\t\ti++;\r\n\t}\r\n\tfor(c=0,i=i-1;i>=0;i--,c++)\r\n\t{\r\n\t\tb[c]=a[i];\r\n\t}\r\n\tprintf(\"%d\\n\",j);\r\n\tfor(i=0;i<j;i++)\r\n\t{\r\n\t\tif(i==j-1)\r\n\t\tprintf(\"%d\\n\",b[i]);\r\n\t\telse\r\n\t\tprintf(\"%d \",b[i]);\r\n\t}\r\n\tfor(i=0;i<j;i++)\r\n\t{\r\n\t\tif(i==j-1)\r\n\t\tprintf(\"%d\\n\",a[i]);\r\n\t\telse\r\n\t\tprintf(\"%d \",a[i]);\r\n\t}\r\n}"
  },
  "1919": {
    "sid": 2480906,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100],n,m,i,j=0,j1;\r\n\tscanf(\"%d %d\",&n,&m);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ta[i]=i+1;\r\n\t}\r\n\tfor(i=1;i<n;i++)\r\n\t{\r\n\t\tj1=0;\r\n\t\tfor(;j1<m;)\r\n\t\t{\r\n\t\t    if(j==n)\r\n\t\t    j=0;\r\n\t\t\tif(a[j]==0)\r\n\t\t\t{\r\n\t\t\t\tj++;\r\n\t\t\t\tcontinue;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj1++;\r\n\t\t\t}\r\n\t\t\tj++;\r\n\t\t\tif(j1==m)\r\n\t    \ta[j-1]=0;\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]!=0)\r\n\t\tprintf(\"%d \",a[i]);\r\n\t}\r\n}"
  },
  "3052": {
    "sid": 2480905,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint a(int x)\r\n{ \r\n    int y;\r\n\tif(x==1)\r\n\ty+=10;\r\n\telse\r\n\ty=a(x-1)+2; \r\n\treturn y;\r\n}\r\nint main()\r\n{\r\n\tint a(int); \r\n \tint x,y;\r\n \ty=a(5);\r\n \tprintf(\"%d\",y);\r\n}"
  },
  "1820": {
    "sid": 2480904,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i,j,t,a[100];\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n    \tif(n==0)\r\n    \tbreak; \r\n    \tfor(i=0;i<n;i++)\r\n    \t{\r\n        \tscanf(\"%d\",&a[i]);\r\n\t\t}\r\n    \tfor(i=0;i<n;i++)\r\n    \t{\r\n\t    \tfor(j=0;j<n-i-1;j++)\r\n        \t{\r\n            \tif(a[j]*a[j]<a[j+1]*a[j+1])\r\n            \t{\r\n\t\t        \tt=a[j];\r\n\t            \ta[j]=a[j+1];\r\n\t            \ta[j+1]=t;\r\n\t            }\r\n     \t    }\r\n     \t}\r\n    \tfor(i=0;i<n;i++)\r\n        {\r\n            printf(\"%d \",a[i]);\r\n\t\t}\r\n        printf(\"\\n\");\r\n    }\r\n}"
  },
  "3053": {
    "sid": 2480902,
    "code": "C",
    "content": "#include<stdio.h>\r\nint p(int n,float x)\r\n{\r\n\tif(n==0)\r\n\treturn 1;\r\n\telse if(n==1)\r\n\treturn x;\r\n\telse\r\n\treturn ((2*n-1)-(p(n-1,x)-(n-1)*p(n-2,x)/n));\r\n}\r\nint main()\r\n{\r\n\tfloat x,y;\r\n\tint n;\r\n\tscanf(\"%d %f\",&n,&x);\r\n\ty=p(n,x);\r\n\tprintf(\"%.2f\",y);\r\n}"
  },
  "3878": {
    "sid": 2480900,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h> \r\nint er(int n)\r\n{\r\n\tint a;\r\n\ta=n%2;\r\n    if(n>=2)\r\n\ter(n/2);\r\n\tputchar(a?'1':'0');\r\n}\r\nint main(int argc, char *argv[])\r\n{ \r\n   int n; \r\n   scanf(\"%d\",&n); \r\n   er(n);\r\n   return 0; \r\n} "
  },
  "1541": {
    "sid": 2480470,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint b,i;\r\n\tgets(a);\r\n\tfor(i=0;i<=100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tb=a[i];\r\n\t\tif(a[i]>='a'&&a[i]<'z')\r\n\t    {\r\n  \t\t\tb=b+1;\r\n  \t\t\ta[i]=b;\r\n    \t}\r\n    \tif(a[i]=='z')\r\n    \ta[i]='a';\r\n\t}\r\n\tfor(i=0;i<=100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n}"
  },
  "1526": {
    "sid": 2480469,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint max(int a,int b);\r\nint min(int a,int b);\r\nint main()\r\n{\r\n\tint a,a1,f,f1;\r\n\tscanf(\"%d%d\",&a,&a1);\r\n\tf=max(a,a1);\r\n\tf1=min(a,a1);\r\n\tprintf(\"%d %d\",f,f1);\r\n}\r\nint max(int a,int b)\r\n{\r\n\tint m,i,n;\r\n\tm=a>b?b:a;\r\n\tfor(i=m;i>=0;i--)\r\n\t{\r\n\t\tif(a%i==0&&b%i==0)\r\n\t\t{\r\n\t\t\tn=i;\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\treturn n;\r\n}\r\nint min(int a,int b)\r\n{\r\n\tint x,y,z;\r\n\ty=a>b?a:b;\r\n\tfor(x=y;x<=a*b;x++)\r\n\t{\r\n\t\tif(x%a==0&&x%b==0)\r\n\t\t{\r\n\t\t\tz=x;\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\treturn z;\r\n}"
  },
  "1529": {
    "sid": 2480468,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,a[3][3];\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<3;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[j][i]);\r\n\t\t}\r\n\t} \r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<3;j++)\r\n\t\t{\r\n\t\t\tprintf(\"%d \",a[i][j]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n} "
  },
  "1531": {
    "sid": 2480467,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tchar a[200],b[100];\r\n\tgets(a);\r\n\tgets(b);\r\n\tfor(i=0;i<200&&a[i]!='\\0';i++)\r\n\tprintf(\"%c\",a[i]);\r\n\tfor(i=0;i<100&&b[i]!='\\0';i++)\r\n\tprintf(\"%c\",b[i]);\r\n}"
  },
  "1527": {
    "sid": 2480466,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint da(float a,float b,float c);\r\nint deng(float a,float b,float c);\r\nint xiao(float a,float b,float c);\r\nint da(float a,float b,float c)//\u5927\u4e8e\u96f6\u7684\u60c5\u51b5 \r\n{\r\n\tfloat d,x1,x2;\r\n\td=(float)sqrt(b*b-4*a*c);\r\n\tx1=(-b+d)/(2*a);\r\n\tx2=(-b-d)/(2*a);\r\n\tprintf(\"x1=%.3f x2=%.3f\",x1,x2);\r\n}\r\nint deng(float a,float b,float c)//\u7b49\u4e8e\u96f6\u7684\u60c5\u51b5 \r\n{\r\n\tfloat x;\r\n\tx=(float)((-b)/(2*a));\r\n\tprintf(\"x1=%.3f x2=%.3f\",x,x);\r\n}\r\nint xiao(float a,float b,float c)//\u5c0f\u4e8e\u96f6\u7684\u60c5\u51b5\uff08\u865a\u6839\uff09 \r\n{\r\n\tfloat d,x;\r\n\td=(float)sqrt(-(b*b-4*a*c))/(2*a);\r\n\tx=(float)((-b)/(2*a));\r\n\tprintf(\"x1=%.3f+%.3fi x2=%.3f-%.3fi\",x,d,x,d);\r\n}\r\nint main()\r\n{\r\n\tfloat d2,i,j,m;\r\n\tscanf(\"%f%f%f\",&i,&j,&m);\r\n\t/*if(i==0)\r\n\t{\r\n\t\tif(j==0)\r\n\t\t{\r\n\t\t\tif(m==0)\r\n\t\t\t{\r\n                printf(\"\");//\u65b9\u7a0b\u7684\u6839\u662f\u6240\u6709\u5b9e\u6570\r\n\t\t\t    return 0;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\"\");//\u8be5\u65b9\u7a0b\u65e0\u6839\r\n\t\t\t\treturn 0;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tprintf(\"x=%.3f\",-m/j);//\u4e00\u5143\u4e00\u6b21\u65b9\u7a0b \r\n\t\t\treturn 0;\r\n\t\t}\r\n\t}*/\r\n\td2=j*j-4*i*m;\r\n\tif(d2>0)\r\n\tda(i,j,m);\r\n\telse if(d2==0)\r\n\tdeng(i,j,m);\r\n\telse\r\n\txiao(i,j,m);\r\n}"
  },
  "1523": {
    "sid": 2480464,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[3][3],i,s=0,s1=0,j,m,n;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<3;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\ts=s+a[i][i];\r\n\t}\r\n\tfor(i=0,j=2;i<3;i++,j--)\r\n\t{\r\n\t\ts1=s1+a[i][j];\r\n\t}\r\n\tprintf(\"%d %d\",s,s1);\r\n}"
  },
  "1534": {
    "sid": 2480463,
    "code": "C",
    "content": "#include<stdio.h>\r\nint pan(char a[])\r\n{\r\n\tint i,a1=0,b=0,c=0,d=0;\r\n\tfor(i=0;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tif(a[i]>='A'&&a[i]<='Z'||a[i]>='a'&&a[i]<='z')\r\n\t\ta1++;\r\n\t    else if(a[i]>='0'&&a[i]<='9')\r\n\t\tb++;\r\n\t\telse if(a[i]==' ')\r\n\t\tc++;\r\n\t\telse\r\n\t\td++;\r\n\t}\r\n\tprintf(\"%d %d %d %d \",a1,b,c,d);\r\n}\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tpan(a);\r\n}"
  },
  "1516": {
    "sid": 2480462,
    "code": "C++",
    "content": "#include <stdio.h>\r\n#include <stdlib.h>\r\n \r\nint main()\r\n{\r\n    int N,j,i,sum,k;\r\n \r\n    scanf(\"%d\",&N);\r\n \r\n    for(i=2;i<N;i++)\r\n    {\r\n        sum=0;\r\n        for(j=1;j<i;j++)\r\n        {\r\n            if(i%j==0)\r\n            {\r\n                sum=sum+j;\r\n            }\r\n        }\r\n        if(sum==i)\r\n        {\r\n            printf(\"%d its fastors are\",i);\r\n            for(k=1;k<i;k++)\r\n            {\r\n                if(i%k==0)\r\n                {\r\n                    printf(\" %d\",k);\r\n                }\r\n            }\r\n            printf(\"\\n\");\r\n        }\r\n \r\n    }\r\n \r\n \r\n \r\n    return 0;\r\n}\r\n"
  },
  "1528": {
    "sid": 2480461,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint pri(int x)\r\n{\r\n\tint i;\r\n\tfor(i=1;i<=(x+1)/2;i++)\r\n\t{\r\n\t\tif(x%i==0)\r\n\t\t{\r\n\t\t\tprintf(\"not prime\");\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\tif(i==(x+1)/2)\r\n\tprintf(\"prime\");\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tpri(a);\r\n}"
  },
  "1520": {
    "sid": 2480460,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n double x1,x2,a;\r\n scanf(\"%lf\",&a); \r\n  x2=1.0;\r\n  do\r\n  {\r\n   x1=x2;\r\n   x2=0.5*(x1+a/x1);\r\n  }\r\n  while(fabs(x2-x1)>=1e-5);\r\n  printf(\"%.3f\\n\",x2);\r\n return 0;\r\n}\r\n"
  },
  "1533": {
    "sid": 2480459,
    "code": "C",
    "content": "#include<stdio.h>\r\nint shu(int x)\r\n{\r\n\tint i,j,m,n;\r\n\ti=x/1000;\r\n\tj=x%1000/100;\r\n\tm=x%1000%100/10;\r\n\tn=x%10;\r\n\tprintf(\"%d %d %d %d\",i,j,m,n);\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tshu(n);\r\n}"
  },
  "1536": {
    "sid": 2480458,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#define pan(a,b,c) c=a%b\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tpan(a,b,c);\r\n\tprintf(\"%d\",c);\r\n}"
  },
  "1517": {
    "sid": 2480457,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat j,i,m=0,x=2,y=1;\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=0;i<a;i++)\r\n\t{\r\n\t\tm=m+(x/y);\r\n\t\tj=x;\r\n\t\tx=x+y;\r\n\t\ty=j;\r\n\t}\r\n\tprintf(\"%.2f\",m);\r\n\t\r\n} "
  },
  "1519": {
    "sid": 2480456,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,x,y=1;\r\n\tscanf(\"%d\",&x);\r\n\tfor(i=x;i>1;i--)\r\n\t{\r\n\t\ty=(y+1)*2;\r\n\t}\r\n\tprintf(\"%d\",y);\r\n}"
  },
  "1542": {
    "sid": 2480455,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,max,min,sum;\r\n\tscanf(\"%d%d%d\",&a,&b,&c);\r\n\tmax=a>b?a:b;\r\n\tmax=max>c?max:c;\r\n\tmin=a<b?a:b;\r\n\tmin=min<c?min:c;\r\n\tsum=(a+b+c)-min-max;\r\n\tprintf(\"%d %d %d\",min,sum,max); \r\n}"
  },
  "1522": {
    "sid": 2480454,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[10],i,j,m=0,n=0;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t} \r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tfor(j=i+1;j<10;j++)\r\n\t\t{\r\n\t\t\tif(a[i]>a[j])\r\n\t\t\t{\r\n\t\t\t\tm=a[i];\r\n\t\t\t\ta[i]=a[j];\r\n\t\t\t\ta[j]=m;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tprintf(\"%d\\n\",a[i]);\r\n\t}\r\n}"
  },
  "1532": {
    "sid": 2480453,
    "code": "C",
    "content": "#include<stdio.h>\r\nint bian(char x)\r\n{\r\n\tif(x=='a'||x=='e'||x=='i'||x=='o'||x=='u')\r\n\treturn 1;\r\n\telse\r\n\treturn 0;\r\n}\r\nint main()\r\n{\r\n\tint i,b;\r\n\tchar a[100];\r\n\tgets(a);\r\n\tfor(i=0;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tb=bian(a[i]);\r\n\t\tif(b==1)\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n \r\n}"
  },
  "1539": {
    "sid": 2480452,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat n;\r\n\tint i,j;\r\n\tscanf(\"%f\",&n);\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<=i;j++)\r\n\t\t{\r\n\t\t\tif(j==i)\r\n\t\t\tprintf(\"%6.2f\",n);\r\n\t\t\telse\r\n\t\t\tprintf(\"%6.2f \",n);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t} \r\n}"
  },
  "1518": {
    "sid": 2480451,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat h,c,i,j=0;\r\n\tscanf(\"%f%f\",&h,&c);\r\n\tfor(i=1;i<=c;i++)\r\n\t{\r\n\t\tif(i==1)\r\n \t\tj=j+h;\r\n \t\telse\r\n \t\tj=j+2*h;\r\n\t\th=h/2;\t\r\n\t}\r\n\tprintf(\"%.2f %.2f\",h,j);\r\n}\r\n"
  },
  "1521": {
    "sid": 2480450,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,n;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=2;i<=n;i++)\r\n\t{\r\n\t\tfor(j=2;j<=(i+1)/2;j++)\r\n\t\t{\r\n\t\t\tif(i%j==0)\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tif(j==(i+1)/2+1)\r\n\t\t{\r\n\t\t\tprintf(\"%d\\n\",i);\r\n\t\t}\r\n\t\t\r\n\t}\r\n}"
  },
  "1540": {
    "sid": 2480449,
    "code": "C",
    "content": "#include<stdio.h>\r\n#define T(a,b,c) (a>b?a:b)>c?(a>b?a:b):c\r\nint A(float a,float b,float c)\r\n{\r\n\tint d;\r\n\td=a>b?a:b;\r\n\td=d>c?d:c;\r\n\treturn d;\r\n}\r\nint main()\r\n{\r\n\tfloat a,b,c,d,d1;\r\n\tscanf(\"%f %f %f\",&a,&b,&c);\r\n\td=A(a,b,c);\r\n\tprintf(\"%.3f\\n\",d);\r\n\td1=T(a,b,c);\r\n\tprintf(\"%.3f\",d1);\r\n} "
  },
  "1514": {
    "sid": 2480447,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat i,i1=0,j,j1=0,m,m1=0,n,a,b,c;\r\n\tscanf(\"%f%f%f\",&a,&b,&c);\r\n\tfor(i=1;i<=a;i++)\r\n\t{\r\n\t\ti1=i1+i;\r\n\t}\r\n\tfor(j=1;j<=b;j++)\r\n\t{\r\n\t\tj1=j1+j*j;\r\n\t}\r\n\tfor(m=1;m<=c;m++)\r\n\t{\r\n\t\tm1=m1+(1/m);\r\n\t}\r\n\tn=i1+j1+m1;\r\n\tprintf(\"%.2f\",n);\r\n}"
  },
  "1010": {
    "sid": 2480445,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,y=0;\r\n    scanf(\"%d\",&n);\r\n    int b[n];\r\n    for(i=0;i<n;i++)\r\n    {\r\n    \tscanf(\"%d\",&m);\r\n    \tint a[n][m];\r\n    \tfor(j=0;j<m;j++)\r\n    \t{\r\n\t    \tscanf(\"%d\",&a[i][j]);\r\n\t    \ty=y+a[i][j];\r\n\t    }\r\n\t    b[i]=y;\r\n\t    y=0;\r\n    }\r\n    for(i=0;i<n;i++)\r\n    {\r\n    \tprintf(\"%d\",b[i]);\r\n    \tprintf(\"\\n\\n\");\r\n    }\r\n\t\r\n}"
  },
  "1009": {
    "sid": 2480444,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\twhile(~(scanf(\"%d %d\",&a,&b)))\r\n\t{\r\n\t\tc=a+b;\r\n\t\tprintf(\"%d\\n\\n\",c);\r\n\t}\r\n}"
  },
  "1008": {
    "sid": 2480442,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n;\r\n    while(~(scanf(\"%d\",&n)))\r\n    {\r\n    \tint a[n];\r\n    \tif(n==0)\r\n    \tbreak;\r\n    \tj=0;\r\n    \tfor(i=0;i<n;i++)\r\n    \t{\r\n\t    \tscanf(\"%d\",&a[i]);\r\n\t    \tj=j+a[i];\r\n\t    }\r\n\t    printf(\"%d\\n\",j);\r\n    }\r\n}"
  },
  "1007": {
    "sid": 2480441,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,y=0;\r\n    scanf(\"%d\",&n);\r\n    int b[n];\r\n    for(i=0;i<n;i++)\r\n    {\r\n    \tscanf(\"%d\",&m);\r\n    \tint a[n][m];\r\n    \tfor(j=0;j<m;j++)\r\n    \t{\r\n\t    \tscanf(\"%d\",&a[i][j]);\r\n\t    \ty=y+a[i][j];\r\n\t    }\r\n\t    b[i]=y;\r\n\t    y=0;\r\n    }\r\n    for(i=0;i<n;i++)\r\n    {\r\n    \tprintf(\"%d\",b[i]);\r\n    \tprintf(\"\\n\");\r\n    }\r\n\t\r\n}"
  },
  "1006": {
    "sid": 2480440,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n;\r\n    while(~(scanf(\"%d\",&n)))\r\n    {\r\n    \tint a[n];\r\n    \tif(n==0)\r\n    \tbreak;\r\n    \tj=0;\r\n    \tfor(i=0;i<n;i++)\r\n    \t{\r\n\t    \tscanf(\"%d\",&a[i]);\r\n\t    \tj=j+a[i];\r\n\t    }\r\n\t    printf(\"%d\\n\",j);\r\n    }\r\n\t\r\n\t\r\n}"
  },
  "1005": {
    "sid": 2480439,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\twhile(~(scanf(\"%d %d\",&a,&b)))\r\n\t{\r\n\t\tif(a==0&&b==0)\r\n\t\tbreak;\r\n\t\tc=a+b;\r\n\t\tprintf(\"%d\\n\",c);\r\n\t}\r\n}"
  },
  "1004": {
    "sid": 2480438,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i,a,b;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tscanf(\"%d %d\",&a,&b);\r\n\t\ta=a+b;\r\n\t\tprintf(\"%d\\n\",a); \r\n\t}\r\n} "
  },
  "1003": {
    "sid": 2480437,
    "code": "C++",
    "content": "#include <stdio.h>\r\nint main()\r\n{\r\nint a,b;\r\nwhile(scanf(\"%d %d\",&a, &b) != EOF)\r\nprintf(\"%d\\n\",a+b);\r\nreturn 0;\r\n}"
  },
  "1000": {
    "sid": 2480435,
    "code": "C++",
    "content": "#include <stdio.h> \r\n\r\nint main() \r\n\r\n{ \r\n\r\n    int a,b; \r\n\r\n    scanf(\"%d %d\",&a, &b); \r\n\r\n    printf(\"%d\\n\",a+b); \r\n\r\n    return 0; \r\n\r\n} "
  },
  "1842": {
    "sid": 2480432,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"Hello World!\\n\");\r\n} "
  },
  "1845": {
    "sid": 2480431,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a;\r\n\ta=getchar();\r\n\tputchar(a);\r\n}"
  },
  "3627": {
    "sid": 2480430,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,m,n,i;\r\n\tscanf(\"%d\",&a);\r\n\tm=a/1000;\r\n\tn=a/100;\r\n\ti=a/10;\r\n\tif(m!=0)\r\n\tprintf(\"4\");\r\n    else if(m==0&&n!=0)\r\n\tprintf(\"3\");  \r\n\telse if(m==0&&n==0&&i!=0)\r\n\tprintf(\"2\");\r\n\telse\r\n\tprintf(\"1\");\r\n}"
  },
  "1875": {
    "sid": 2480429,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tif(a>b)\r\n\tprintf(\"max=%d\",a);\r\n\telse\r\n\tprintf(\"max=%d\",b);\r\n}"
  },
  "3626": {
    "sid": 2480428,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint b;\r\n\tscanf(\"%d\",&b);\r\n\tswitch(b)\r\n\t{\r\n\tcase 1:printf(\"\u4e00\");break;\r\n    case 2:printf(\"\u4e8c\");break;\r\n    case 3:printf(\"\u4e09\");break;\r\n    case 4:printf(\"\u56db\");break;\r\n    case 5:printf(\"\u4e94\");break;\r\n    case 6:printf(\"\u516d\");break;\r\n    case 7:printf(\"\u4e03\");\r\n\t}\r\n}"
  },
  "3099": {
    "sid": 2480427,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a=1.5,b=1.35,c=1.18,i,f;\r\n\tchar x,y;\r\n\tscanf(\"%f %c %c\",&i,&x,&y);\r\n\tswitch(x)\r\n\t{\r\n\t\tcase'a':\r\n\t\t{\r\n\t\t\tif(y=='m')\r\n\t\t\tf=a*0.95*i;\r\n\t\t    if(y=='e')\r\n\t\t\tf=a*0.9*i;\r\n\t\t\tif(y=='f')\r\n\t\t\tf=a*i;\r\n\t\t}break;\r\n\t\tcase'b':\r\n\t\t{\r\n\t\t\tif(y=='m')\r\n\t\t\tf=b*0.95*i;\r\n\t\t    if(y=='e')\r\n\t\t\tf=b*0.9*i;\r\n\t\t\tif(y=='f')\r\n\t\t\tf=b*i;\r\n\t\t}break;\r\n\t\tcase'c':\r\n\t\t{\r\n\t\t\tif(y=='m')\r\n\t\t\tf=c*0.95*i;\r\n\t\t    if(y=='e')\r\n\t\t\tf=c*0.9*i;\r\n\t\t\tif(y=='f')\r\n\t\t\tf=c*i;\r\n\t\t}break;\r\n\t}\r\n\tprintf(\"%.2f\",f);\r\n} "
  },
  "1011": {
    "sid": 2480424,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i=0,j=0;\r\n\tchar m,str[100];\r\n\twhile(~(m=getchar())&&m!='\\n')\r\n\t{\r\n\t\tstr[i]=m;\r\n\t\ti++;\r\n\t}\r\n\tfor(j=i-1;j>=0;j--)\r\n\tprintf(\"%c\",str[j]);\r\n}"
  },
  "1525": {
    "sid": 2480423,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint q,w,e,r,t,y,u,i,o,p;\r\n\tscanf(\"%d %d %d %d %d %d %d %d %d %d\",&q,&w,&e,&r,&t,&y,&u,&i,&o,&p);\r\n\tprintf(\"%d %d %d %d %d %d %d %d %d %d\",p,o,i,u,y,t,r,e,w,q);\r\n}"
  },
  "1512": {
    "sid": 2480422,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b=0,i,j=2,m=0;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=1;i<=a;i++)\r\n\t{\r\n\t\tb=b+j;\r\n\t\tj=j*10;\r\n\t\tm+=b;\r\n\t}\r\n\tprintf(\"%d\",m);\r\n}"
  },
  "3639": {
    "sid": 2480421,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d\",&a);\r\n\tif(a%5==0&&a%7==0)\r\n\tprintf(\"yes\");\r\n\telse\r\n\tprintf(\"no\");\r\n}"
  },
  "3802": {
    "sid": 2480420,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,i,j=1,m=0;\r\n\tscanf(\"%d\",&a);\r\n\tfor(i=1;i<=a;i++)\r\n\t{\r\n    \tj=j*(-i); \r\n    \tm=m+(-j);\r\n\t}\r\n\tprintf(\"%d\",m);\r\n\r\n} "
  },
  "3646": {
    "sid": 2480419,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    char a;\r\n    scanf(\"%c\",&a);\r\n    if(a>='a'&&a<='z')\r\n    a=a-32;\r\n    else if(a>='A'&&a<='B')\r\n    a=a+32;\r\n    else\r\n    a=a;\r\n    printf(\"%c\\n\",a);\r\n}\r\n"
  },
  "1819": {
    "sid": 2480418,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(~scanf(\"%d\",&n))\r\n\t{\r\n\t\tint i,j=1,a[n];\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i]);\r\n\t\t}\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tif(a[i]%2==1)\r\n\t\t\tj=j*a[i];\r\n\t\t}\r\n\t\tprintf(\"%d\\n\",j);\r\n\t}\r\n\t\r\n}"
  },
  "1826": {
    "sid": 2480417,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i,j=0,c=0,a=0;\r\n\twhile(~(scanf(\"%d\",&n)))\r\n\t{\r\n\t\tif(n==0)\r\n\t\tbreak;\r\n\t\ta=0;\r\n\t\tc=0;\r\n\t\tj=0;\r\n\t\tfloat b[n];\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%f\",&b[i]);\r\n\t\t}\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tif(b[i]>0)\r\n\t\t\ta++;\r\n\t\t    else if(b[i]==0)\r\n\t\t\tc++;\r\n\t\t\telse\r\n\t\t\tj++;\r\n\t\t}\r\n\t\tprintf(\"%d %d %d\\n\",j,c,a);\r\n\t}\r\n}"
  },
  "1530": {
    "sid": 2480415,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint i=0,j,m,n;\r\n\tgets(a);\r\n\tfor(i=0;i<100&&a[i]!='\\0';)\r\n\t{\r\n\t\ti++;\r\n\t}\r\n\tfor(i=i-1;i>=0;i--)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n} "
  },
  "1524": {
    "sid": 2480414,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint b=1,i,j,m,n,a[10];\r\n\tchar c;\r\n\tfor(i=0;i<9;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n    scanf(\"%d\",&n);\r\n\tfor(i=0;i<9;i++)\r\n\t{\r\n\t\tif(n<a[i])\r\n\t\tbreak;\r\n\t}\r\n\tfor(;i<10;i++,b++)\r\n\t{\r\n\t\tif(b%2==1)\r\n\t\t{\r\n\t\t\tm=a[i];\r\n\t\t\ta[i]=n;\r\n\t\t}\r\n\t\tif(b%2==0)\r\n\t\t{\r\n\t\t\tn=a[i];\r\n\t\t\ta[i]=m;\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tprintf(\"%d\\n\",a[i]);\r\n\t}\r\n}\r\n "
  },
  "1535": {
    "sid": 2480413,
    "code": "C",
    "content": "#include<stdio.h>\r\n#define T(a,b) {int c;c=a;a=b;b=c;}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d %d\",&a,&b);\r\n\tT(a,b);\r\n\tprintf(\"%d %d\",a,b);\r\n}"
  },
  "1538": {
    "sid": 2480412,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#define LEAP_YEAR(y) y%4==0&&y%100!=0||y%400==0\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tif(LEAP_YEAR(a))\r\n\tprintf(\"L\");\r\n\telse\r\n\tprintf(\"N\"); \r\n}"
  },
  "1927": {
    "sid": 2480411,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint b[100];\r\n\tint i,j,m,n;\r\n\tgets(a);\r\n\tfor(i=0;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tb[i]=a[i];\r\n\t}\r\n\tif((b[0]>='A'&&b[0]<='Z')||(b[0]>='a'&&b[0]<='z')||b[0]=='_')\r\n\t{\r\n\t\t;\r\n\t}\r\n\telse\r\n\t{\r\n\t\tprintf(\"NO\");\r\n\t\treturn 0;\r\n\t}\r\n\tfor(i=1;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tif((b[i]>='A'&&b[i]<='Z')||(b[i]>='a'&&b[i]<='z')||(b[i]>='0'&&b[i]<='9')||b[i]=='_')\r\n\t\t{\r\n\t\t\tcontinue;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tprintf(\"NO\");\r\n\t\t\treturn 0;\r\n\t\t}\r\n\t}\r\n\tprintf(\"YES\");\r\n}"
  },
  "3628": {
    "sid": 2480410,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint b=0,i=0,j=0,m=0,n;\r\n\tscanf(\"%s\",&a);\r\n\tfor(i=0;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tn=a[i];\r\n\t\tif(n>=65&&n<=90||n>=97&&n<=122)\r\n\t\tb++;\r\n\t\telse if(n>=48&&n<=57)\r\n\t\tj++;\r\n        else\r\n\t\tm++;\t\r\n\t}\r\n\tprintf(\"%d %d %d\",b,j,m);\r\n} "
  },
  "3054": {
    "sid": 2480402,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint max(int a,int b);\r\nint zhao(int x,int y,int i,int j);\r\nint main()\r\n{\r\n   \tint w,r,m,n,a;\r\n   \tscanf(\"%d%d%d%d\",&w,&r,&m,&n);\r\n   \ta=zhao(w,r,m,n);\r\n   \tprintf(\"%d\",a);\r\n}\r\nint zhao(int x,int y,int i,int j)\r\n{\r\n\tint pi;\r\n\tpi=max(x,y)>max(i,j)?max(x,y):max(i,j);\r\n\treturn pi;\r\n}\r\nint max(int a,int b)\r\n{\r\n\treturn a>b?a:b;\r\n}"
  },
  "3055": {
    "sid": 2480401,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int x)\r\n{\r\n\tif(x==1)\r\n\treturn 1;\r\n\telse\r\n\treturn (fac(x-1)*x);\r\n}\r\nint add(int a,int b)\r\n{\r\n\treturn (fac(a)+fac(b));\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tprintf(\"%d\",add(a,b));\r\n}"
  },
  "3069": {
    "sid": 2480400,
    "code": "C",
    "content": "#include<stdio.h>\r\nint add(int a,int b)\r\n{\r\n\treturn ((a+b)*(a-b));\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tprintf(\"%d\",add(a,b));\r\n}"
  },
  "3071": {
    "sid": 2480399,
    "code": "C",
    "content": "#include<stdio.h>\r\nint add(int x)\r\n{\r\n    int a,b,c,d; \r\n\ta=x/1000;\r\n\tb=x%1000/100;\r\n\tc=x%1000%100/10;\r\n\td=x%10;\r\n\tif(((a*10+b)+(c*10+d))*((a*10+b)+(c*10+d))==x)\r\n\treturn 1;\r\n\telse\r\n\treturn 0;\r\n}\r\nint main()\r\n{\r\n\tint x;\r\n\tscanf(\"%d\",&x);\r\n\tprintf(\"%d\",add(x));\r\n} "
  },
  "3607": {
    "sid": 2480398,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,c,f;\r\n\tchar b;\r\n\tscanf(\"%d%c%d\",&a,&b,&c);\r\n\tswitch(b)\r\n\t{\r\n    case'*':f=a*c;break;\r\n    case'+':f=a+c;break;\r\n    case'%':f=a%c;break;\r\n    case'-':f=a-c;\r\n\t}\r\n    printf(\"%d\",f);\r\n}"
  },
  "3615": {
    "sid": 2480397,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint b;\r\n\tchar a,c;\r\n\tscanf(\"%c%d\",&a,&b);\r\n\tc=a+b;\r\n\tprintf(\"%c\",c);\r\n    \r\n}"
  },
  "1888": {
    "sid": 2480396,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i,j,m,x,y;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&m);\r\n\t\tfor(j=1;j<=m;j++)\r\n\t\t{\r\n\t\t\tfor(x=1;x<=j;x++)\r\n\t\t\tprintf(\"*\");\r\n\t\t\tprintf(\"\\n\");\r\n\t\t}\r\n\t}\r\n}"
  },
  "1933": {
    "sid": 2480394,
    "code": "C",
    "content": "#include<stdio.h>\r\nfloat jc(float x)\r\n{\r\n\tif(x==1)\r\n\treturn 1;\r\n\telse\r\n\treturn (jc(x-1)*x);\r\n} \r\nfloat fac(float x,float y)\r\n{\r\n\treturn jc(x)/(jc(y)*jc(x-y));\r\n}\r\nint main()\r\n{\r\n\tfloat a,b;\r\n\tscanf(\"%f%f\",&a,&b);\r\n\tprintf(\"%.0f\",fac(a,b));\r\n}"
  },
  "3840": {
    "sid": 2480393,
    "code": "C",
    "content": "#include<stdio.h>\r\n#define Max(a,b) a>b?a:b\r\n#define Min(a,b) a>b?b:a\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\t#ifdef Max\r\n\t{\r\n\t\t\tprintf(\"%d\",Max(a,b));\r\n\t\t\treturn 0;\r\n\t}\r\n\t#endif\r\n\tprintf(\"%d\",Min(a,b));\r\n}"
  },
  "3860": {
    "sid": 2480392,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include<stdio.h>\r\n int pan(char a)\r\n {\r\n \tif(a>='a'&&a<='z')\r\n \treturn 2; \r\n \telse if(a>='A'&&a<='Z')\r\n \treturn 1;\r\n \telse\r\n \treturn 0;\r\n } \r\n int main(int argc, char *argv[]) \r\n{ \r\n char c;\r\n c=getchar();\r\n if(pan(c)==1) \r\n { \r\n printf(\"Y\"); \r\n } \r\n else if(pan(c)==2) \r\n{\r\n  printf(\"y\");\r\n} \r\n else if(pan(c)==0) \r\n{ \r\n  printf(\"n\"); \r\n} \r\n   return 0; \r\n} "
  },
  "3866": {
    "sid": 2480391,
    "code": "C",
    "content": "#include<stdio.h>\r\nint pan(int m,int n)\r\n{\r\n\tint i,j;\r\n\tfor(i=m,j=0;i<=n;i++)\r\n\t{\r\n\t\tif(i%3==0&&i%5!=0)\r\n\t\t{\r\n\t\t\tprintf(\"%d\\n\",i);\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tif(j==0)\r\n\tprintf(\"no\");\r\n}\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d,%d\",&m,&n);\r\n\tpan(m,n);\r\n}"
  },
  "3882": {
    "sid": 2480390,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h> \r\nint max(int a,int b,int c)\r\n{\r\n\tint min;\r\n\tmin=a>b?b:a;\r\n\tmin=min>c?c:min;\r\n\tint i,a1,b1,c1;\r\n\tfor(i=min;i>=1;i--)\r\n\t{\r\n\t\tif(a%i==0&&b%i==0&&c%i==0)\r\n\t\t{\r\n\t\t\treturn i;\r\n\t\t}\r\n\t}\r\n}\r\nint main(int argc, char *argv[])\r\n{\r\nint a,b,c;\r\n\r\nscanf(\"%d,%d,%d\",&a,&b,&c);\r\n\r\nprintf(\"%d\",max(a,b,c));\r\n\r\nreturn 0;\r\n\r\n}"
  },
  "3881": {
    "sid": 2480389,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h>\r\nint cf(int x)\r\n{\r\n\tint i,j;\r\n\tfor(i=1;i<=x;i++)\r\n\t{\r\n\t\tfor(j=1;j<=i;j++)\r\n\t\t{\r\n\t\t\tprintf(\"%d*%d=%d \",j,i,j*i);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}\r\nint main(int argc, char *argv[])\r\n\r\n{\r\n\r\n    int n;\r\n\r\n    scanf(\"%d\",&n);\r\n\r\n    cf(n);\r\n\r\n    return 0;\r\n\r\n}"
  },
  "3863": {
    "sid": 2480388,
    "code": "C",
    "content": "#include<stdio.h>\r\nint hui(int m,int n)\r\n{\r\n\tint i,j,a,b,c,d,e,f=0;\r\n\tfor(i=m;i<=n;i++)\r\n\t{\r\n\t\ta=i/10000;\r\n\t\tb=i%10000/1000;\r\n\t\tc=i%10000%1000/100;\r\n\t\td=i%10000%1000%100/10;\r\n\t\te=i%10;\r\n\t\tif(a==e&&b==d)\r\n\t\t{\r\n\t\t\tprintf(\"%d\\n\",i);\t\r\n\t\t\tf++;\r\n\t\t}\r\n\t}\r\n\tif(f==0)\r\n\tprintf(\"no\");\r\n}\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d,%d\",&m,&n);\r\n\thui(m,n);\r\n\treturn 0;\r\n}"
  },
  "3865": {
    "sid": 2480387,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d,%d\",&a,&b);\r\n\tint i,j=a,m=0;\r\n\tfor(i=0;i<=b;i++)\r\n\t{\r\n\t\tj=a;\r\n\t\tj=j+i;\r\n\t\tm=m+j;\r\n\t}\r\n\tprintf(\"%d\",m);\r\n}"
  },
  "3861": {
    "sid": 2480386,
    "code": "C",
    "content": "#include <stdio.h>\r\nvoid huanf(int m,int n,int k)\r\n{\r\n\tint i,j,p;\r\n\tif(m+2*n+5*k<=100)\r\n\t{\r\n\t\tfor(i=m;i<=100;i++)\r\n\t {\r\n\t\tfor(j=n;j<=50;j++)\r\n\t\t{\r\n\t\t\tfor(p=k;p<=20;p++)\r\n\t\t\t{\r\n\t\t\t\tif(i+j*2+p*5==100)\r\n\t\t\t\t{\r\n\t\t\t\t\tprintf(\"%d %d %d\\n\",p,j,i);\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}\r\n\t }\r\n\t}\r\n\t\r\n} \r\nint main()\r\n{\r\n\tint n,m,k;\r\n\tscanf(\"%d,%d,%d\",&m,&n,&k);\r\n\thuanf(m,n,k);\r\n}"
  },
  "3868": {
    "sid": 2480385,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a,a1,b=0,i,j,m,n,y,sum,sum1,x[100];\r\n\tscanf(\"%d,%d\",&m,&n);\r\n\tfor(i=m;i<=n;i++)\r\n\t{\r\n\t\ta=i;\r\n\t\ta1=i*i;\r\n\t\tb=0;\r\n\t\tsum1=0;\r\n\t\tsum=0;\r\n\t\twhile(a!=0)\r\n\t\t{\r\n\t\t\tb++;\r\n\t\t\ta=a/10;\r\n\t\t}\r\n\t\tfor(y=0;y<b;y++)\r\n\t\t{\r\n\t\t\tx[y]=a1%10;\r\n\t\t\ta1=a1/10;\r\n\t\t}\r\n\t\tfor(j=0;j<b;j++)\r\n\t\t{\r\n\t\t\tsum1=x[j]*pow(10,j);\r\n\t\t\tsum=sum+sum1;\r\n\t\t}\r\n\t\tif(i==sum)\r\n\t\t{\r\n\t\t\tprintf(\"%d\\n\",i);\r\n\t\t}\r\n\t}\t\t\r\n}"
  },
  "3869": {
    "sid": 2480384,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat j=0,m,n,y=0,sum1=0,sum2=0,s1,s2;\r\n\tint i;\r\n\twhile(~(scanf(\"%d\",&i)))\r\n\t{\r\n\t\tif(i==0)\r\n\t\tbreak;\r\n\t\tif(i%2==0)\r\n\t\t{\r\n\t\t\tsum2=sum2+i;\r\n\t\t\ty++;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tsum1=sum1+i;\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tif(j==0)\r\n\ts1=0;\r\n\telse\r\n\ts1=sum1/j;\r\n\tif(y==0)\r\n\ts2=0;\r\n\telse\r\n\ts2=sum2/y;\r\n\t\r\n\tprintf(\"%.2f,%.2f\",s1,s2);\r\n}"
  },
  "3825": {
    "sid": 2480383,
    "code": "C",
    "content": "#include <stdio.h>\r#define DEBUG //for test\n#include <stdio.h>\r#define DEBUG //for test\n#include <stdio.h>\r\n\r\n#define DEBUG \r\n\r\n\r\n\r\nint main()\r\n\r\n{\r\n\r\n#ifdef DEBUG\r\nprintf(\"Not debugging\\n\");\r\n#else\r\n\r\nprintf(\"Debugging\\n\");\r\n#endif\r\n\r\nprintf(\"Running\");\r\n\r\nreturn 0;\r\n\r\n}"
  },
  "3883": {
    "sid": 2480381,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h>\r\n\r\nint shui(int a)\r\n{\r\n\tint i,j,m;\r\n\ti=a/100;\r\n\tj=a%100/10;\r\n\tm=a%10;\r\n\tif(i*i*i+j*j*j+m*m*m==a)\r\n\treturn 1;\r\n\telse\r\n\treturn 0;\r\n} \r\n\r\nint main(int argc, char *argv[])\r\n\r\n{\r\n\r\n    int start,end;\r\n\r\n    scanf(\"%d,%d\",&start,&end);\r\n\r\n    while(start<=end)\r\n\r\n   {\r\n\r\n        if(shui(start)==1)\r\n\r\n        {\r\n\r\n            printf(\"%d\\n\",start);\r\n\r\n        }\r\n\r\n        start++;\r\n\r\n    }\r\n\r\n    return 0;\r\n\r\n}"
  },
  "3056": {
    "sid": 2480380,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[10],b[10];\r\n\tint *p,*q;\r\n\tp=a;\r\n\tq=b;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",p+i);\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\t*(q+i)=*(p+i);\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==9)\r\n\t\tprintf(\"%d\",*(q+i));\r\n\t\telse\r\n\t\tprintf(\"%d \",*(q+i));\r\n\t}\r\n}"
  },
  "3057": {
    "sid": 2480379,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,j;\r\n\tscanf(\"%d\",&n);\r\n\tint a[n],b[n];\r\n\tint i;\r\n\tint *p,*q;\r\n\tp=a;\r\n\tq=b;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",p+i);\r\n\t}\r\n\tfor(i=n-1,j=0;i>=0;i--,j++)\r\n\t{\r\n\t\t*(q+i)=*(p+j);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tprintf(\"%d \",*(q+i));\r\n\t}\r\n\t\r\n}"
  },
  "3770": {
    "sid": 2480378,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint b=0,i=0,j=0,m=0,k=0,n;\r\n\tgets(a);\r\n\tfor(i=0;i<100&&a[i]!='\\0';i++)\r\n\t{\r\n\t\tn=a[i];\r\n\t\tif(n>=65&&n<=90||n>=97&&n<=122)\r\n\t\tb++;\r\n\t\telse if(n>=48&&n<=57)\r\n\t\tj++;\r\n\t\telse if(n==32)\r\n\t\tm++;\r\n        else\r\n\t\tk++;\t\r\n\t}\r\n\tprintf(\"%d %d %d %d\",b,j,m,k);\r\n} "
  },
  "3062": {
    "sid": 2480377,
    "code": "C",
    "content": "#include<stdio.h>\r\nint hou(char* q, int n)\r\n{\r\n\tchar* p;\r\n\tint i, j;\r\n\tfor (i = 0; *(q + i) != 0; i++)\r\n\t{\r\n\r\n\t}\r\n\tfor (j = n; j < i; j++)\r\n\t{\r\n\t\tprintf(\"%c\", *(q + j));\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint n;\r\n\tscanf(\"%d\", &n);\r\n    getchar();\r\n\tgets(a);\r\n\thou(a, n);\r\n}"
  },
  "3063": {
    "sid": 2480376,
    "code": "C",
    "content": "#include<stdio.h>\r\nint pan(char *p)\r\n{\r\n\tint i;\r\n\tfor(i=0;*(p+i)!='\\0';i++)\r\n\t{\r\n\t\t\tif(*(p+i)=='k')\r\n\t\t\t{\r\n\t\t\t\treturn 1;\r\n\t\t\t}\r\n\t}\r\n\treturn 0;\r\n} \r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tif(pan(a)==1)\r\n\t{\r\n\t\tprintf(\"yes\");\r\n\t}\r\n\telse\r\n\tprintf(\"no\");\r\n}"
  },
  "3064": {
    "sid": 2480375,
    "code": "C",
    "content": "#include<stdio.h>\r\nfloat jige(float* p)\r\n{\r\n\tfloat j = 0;\r\n\tint i;\r\n\tfor (i = 0; i < 10; i++)\r\n\t{\r\n\t\tif (*(p + i) >= 60)\r\n\t\t{\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\treturn j / 10;\r\n}\r\nint main()\r\n{\r\n\tfloat a[10];\r\n\tint i;\r\n\tfor (i = 0; i < 10; i++)\r\n\t{\r\n\t\tscanf(\"%f\", &a[i]);\r\n\t}\r\n\tprintf(\"%.2f\", jige(a));\r\n\r\n}"
  },
  "3068": {
    "sid": 2480372,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid max(int* p, int  n)\r\n{\r\n\tint i;\r\n\tint tem;\r\n\tfor (i = 0; i < n - 1; i++)\r\n\t{\r\n\t\tif (*(p + i) < *(p + i + 1))\r\n\t\t{\r\n\t\t\ttem = *(p + i + 1);\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\", tem);\r\n}\r\nint main()\r\n{\r\n\tint i, j, m, n;\r\n\tscanf(\"%d%d\", &m, &n);\r\n\tint a[m][n];\r\n\tfor (i = 0; i < m; i++)\r\n\t{\r\n\t\tfor (j = 0; j < n; j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\", &a[i][j]);\r\n\t\t}\r\n\t}\r\n\tmax(a[0], m * n);\r\n}"
  },
  "3773": {
    "sid": 2480367,
    "code": "C",
    "content": "#include<stdio.h>\r\nint f1(int* p)\r\n{\r\n\tint i;\r\n\tint* q;\r\n\tq = p;\r\n\tfor (i = 0; i < 5; i++)\r\n\t{\r\n\t\tif (*(p + i) < *(p + i + 1))\r\n\t\t\t*q = *(p + i + 1);\r\n\t}\r\n\treturn *q;\r\n}\r\nint main()\r\n{\r\n\tint a[5];\r\n\tint i;\r\n\tfor (i = 0; i < 5; i++)\r\n\t{\r\n\t\tscanf(\"%d\", &a[i]);\r\n\t}\r\n\tprintf(\"%d\", f1(a));\r\n\r\n\r\n}"
  },
  "3774": {
    "sid": 2480366,
    "code": "C",
    "content": "#include<stdio.h>\r\nint shu(char(*p)[100])\r\n{\r\n\tint a=0,i,j=0;\r\n\tfor (i = 0; i<3; i++)\r\n\t{\r\n\t\tfor (j = 0; *(*(p + i) + j) != '\\0'; j++)\r\n\t\t{\r\n\t\t\tif (*(*(p + i) + j) == 'm')\r\n\t\t\t{\r\n\t\t\t\ta++;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\treturn a;\r\n}\r\nint main()\r\n{\r\n\tchar a[3][100];\r\n\tint i;\r\n\tfor (i = 0; i < 3; i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tprintf(\"%d\",shu(a));\r\n}"
  },
  "3775": {
    "sid": 2480365,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid f1(char** p, char** q)\r\n{\r\n\tchar* t;\r\n\tt = &(**p);\r\n\t*p = &(**q);\r\n\t*q = t;\r\n}\r\nint main()\r\n{\r\n\tchar* p = \"hello\";\r\n\tchar* p2 = \"world\";\r\n\tf1(&p, &p2);\r\n\tputs(p);\r\n\tputs(p2);\r\n}"
  },
  "3835": {
    "sid": 2480362,
    "code": "C",
    "content": "#include<stdio.h>\r\nint max(int *p)\r\n{\r\n\tint i;\r\n\tint j=*p;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tif(j<*(p+i))\r\n\t\tj=*(p+i);\r\n\t}\r\n\treturn j;\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[3];\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\t\r\n\tprintf(\"%d\",max(a));\r\n} "
  },
  "3848": {
    "sid": 2480361,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid huan(char *p,char *q)\r\n{\r\n\tchar i;\r\n\ti=*p;\r\n\t*p=*q;\r\n\t*q=i;\r\n}\r\nint main()\r\n{\r\n\tchar a,b;\r\n\tscanf(\"%c %c\",&a,&b);\r\n\thuan(&a,&b);\r\n\tprintf(\"%c %c\",a,b);\r\n} "
  },
  "3051": {
    "sid": 2480360,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int a)\r\n{\r\n\tif(a==1)\r\n\treturn 1;\r\n\telse\r\n\treturn fac(a-1)*a;\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n    printf(\"%d\",fac(a));\r\n}"
  },
  "3875": {
    "sid": 2480359,
    "code": "C",
    "content": "#include<stdio.h>\r\nint age(int a)\r\n{\r\n\tif (a == 1)\r\n\t\treturn 1;\r\n\telse\r\n\t\treturn age(a - 1) + 2 * a - 1;\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\", &a);\r\n\tprintf(\"%d\", age(a));\r\n}"
  },
  "2672": {
    "sid": 2480358,
    "code": "C",
    "content": "#include<stdio.h>\r\nint AKM(int m, int n)\r\n{\r\n\tif (m == 0)\r\n\t\treturn n+1;\r\n\telse if (n == 0)\r\n\t\treturn AKM(m - 1, 1);\r\n\telse\r\n\t\treturn AKM(m - 1, AKM(m, n - 1));\r\n}\r\nint main()\r\n{\r\n\tint a, b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tprintf(\"%d\",AKM(a, b));\r\n}"
  },
  "1145": {
    "sid": 2480357,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[256];\r\n\tint sum = 0, i, len;\r\n\twhile (gets(a) && a[0] != '#')\r\n\t{\r\n\t\tsum = 0;\r\n\t\tint j;\r\n\t\tfor (j = 0; a[j] != '\\0'; j++)\r\n\t\t{\r\n\t\t\t;\r\n\t\t}\r\n\t\tfor (i = 0; i < j; i++)\r\n\t\t{\r\n\t\t\tif (a[i] != ' ')\r\n\t\t\t\tsum = sum + (i + 1) * (a[i] - 'A' + 1);\r\n\t\t}\r\n\t\tprintf(\"%d\\n\", sum);\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "2918": {
    "sid": 2480356,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nfloat fac(float m, float n)\r\n{\r\n    float a;\r\n    a = m * m + n * n;\r\n    a = sqrt(a);\r\n    return a;\r\n}\r\nint main()\r\n{\r\n    float a, b;\r\n    scanf(\"%f%f\",&a,&b);\r\n    printf(\"%.2f\",fac(a,b));\r\n}"
  },
  "2919": {
    "sid": 2480355,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint fac(int a)\r\n{\r\n\tint m, n;\r\n\tm = a / 100;\r\n\tn = a % 100;\r\n\tint b;\r\n\tb = (m + n) * (m + n);\r\n\tif (b == a)\r\n\t\treturn b;\r\n\telse\r\n\t\treturn 0;\r\n}\r\nint main()\r\n{\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tprintf(\"%d\",fac(m));\r\n}"
  },
  "1138": {
    "sid": 2480354,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint fac(int x)\r\n{\r\n\tif(x==0)\r\n\treturn 0;\r\n\telse if(x==1)\r\n\treturn 1;\r\n\telse\r\n\treturn fac(x-1)+fac(x-2);\r\n}\r\nint main()\r\n{\r\n\tint i,j=0;\r\n\twhile((scanf(\"%d\",&i))!=EOF&&j<50)\r\n\t{\r\n\t\tprintf(\"%d\\n\",fac(i));\r\n\t\tj++;\r\n\t}\r\n}"
  },
  "1903": {
    "sid": 2480353,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint min(int a,int b)\r\n{\r\n\tint i,j;\r\n\tj=a>b?a:b;\r\n\tfor(i=j;i<a*b;i++)\r\n\t{\r\n\t\tif(i%a==0&&i%b==0)\r\n\t\t{\r\n\t\t\treturn i;\r\n\t\t}\r\n\t}\r\n}\r\nint max(int x,int y)\r\n{\r\n\tint i,j;\r\n\tj=x>y?y:x;\r\n\tfor(i=j;i>=1;i--)\r\n\t{\r\n\t\tif(x%i==0&&y%i==0)\r\n\t\treturn i;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tprintf(\"%d %d\",min(a,b),max(a,b));\r\n}"
  },
  "1915": {
    "sid": 2480352,
    "code": "C++",
    "content": "#include<stdio.h>\r\nfloat f1(int  x)\r\n{\r\n\tfloat sum = 0;\r\n\tfloat i;\r\n\tfor (i = 1; i <= x; i++)\r\n\t{\r\n\t\tsum = sum + (1 / (4 * i - 3)) - (1 / (4 * i - 1));\r\n\t}\r\n\treturn 4 * sum;\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\", &a);\r\n\tprintf(\"%.5f\", f1(a));\r\n}"
  },
  "1935": {
    "sid": 2480351,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[n];\r\n\tint i,sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]%2==0)\r\n\t\tsum=sum+a[i];\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "1878": {
    "sid": 2480350,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"*****\\n*\\n*\\n*\\n*****\");\r\n}"
  },
  "3190": {
    "sid": 2480349,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tif (n == 1 || n == 0)\r\n\t\treturn n;\r\n\telse\r\n\t\treturn fac(n - 1) + n;\r\n}\r\nint f1(int n)\r\n{\r\n\tint sum;\r\n\tsum = fac(n * n);\r\n\treturn sum / n;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tprintf(\"%d\",f1(n));\r\n}"
  },
  "3191": {
    "sid": 2480348,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint p;\r\n\tint n;\r\n\tint t;\r\n\tint a = 0;\r\n\tint i;\r\n\tscanf(\"%d\", &t);\r\n\tif (t <= 100)\r\n\t{\r\n\t\tfor (i = 0; i < t; i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\", &n);\r\n\t\t\tint b[100];\r\n\t\t\tint i;\r\n\t\t\tint y = 0;\r\n\t\t\tfor (i = 0; n != 0; i++)\r\n\t\t\t{\r\n\t\t\t\tb[i] = n % 2;\r\n\t\t\t\tif (b[i] == 1)\r\n\t\t\t\t{\r\n\t\t\t\t\ty++;\r\n\t\t\t\t}\r\n\t\t\t\tn = n / 2;\r\n\t\t\t}\r\n\t\t\tp = y;\r\n\t\t\tprintf(\"%d\\n\", p);\r\n\t\t}\r\n\t}\r\n}\r\n"
  },
  "3871": {
    "sid": 2480347,
    "code": "C++",
    "content": "#include <stdio.h>\r\nfloat monf(float h)\r\n{\r\n\tif(h>120)return 120*84+(h-120)*84*1.15;\r\n\telse if(h<=120&&h>=60)return h*84;\r\n\telse if(h<60&&h>=9)return h*84-700;\r\n\telse if(h<=8)return 0;\r\n}\r\nint main()\r\n{\r\n\tfloat h,m;\r\n\tscanf(\"%f\",&h);\r\n\tm=monf(h);\r\n\tprintf(\"%.2f\",m);\r\n}"
  },
  "3059": {
    "sid": 2480344,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tstruct man{\r\n\t\tchar x[16];\r\n\t\tint a;\r\n\t\tint b;\r\n\t\tint c;\r\n\t\tint d;\r\n\t\tint e;\r\n\t\tint f;\r\n\t\tint aver;\r\n\t\tint sum;\r\n\t}boy;\r\n\tscanf(\"%s%d%d%d%d%d%d\",&boy.x,&boy.a,&boy.b,&boy.c,&boy.d,&boy.e,&boy.f);\r\n\tboy.aver=boy.a+boy.b+boy.c+boy.d+boy.e+boy.f;\r\n\tboy.sum=boy.aver/6;\r\n\tprintf(\"%s %d %d\",boy.x,boy.aver,boy.sum);\r\n}"
  },
  "3701": {
    "sid": 2480342,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tstruct man {\r\n\t\tint a;\r\n\t\tchar x[16];\r\n\t\tfloat i;\r\n\t\tfloat j;\r\n\t\tfloat m;\r\n\t}s[5];\r\n\tint ci;\r\n\tfloat n[5];\r\n\tfloat a1 = 0, b1 = 0, c1 = 0;\r\n\tfor (ci = 0; ci < 5; ci++)\r\n\t{\r\n\t\tscanf(\"%d\", &s[ci].a);\r\n\t\tscanf(\"%s\", &s[ci].x);\r\n\t\tscanf(\"%f\", &s[ci].i);\r\n\t\tscanf(\"%f\", &s[ci].j);\r\n\t\tscanf(\"%f\", &s[ci].m);\r\n\t\tn[ci] = s[ci].i + s[ci].j + s[ci].m;\r\n\t\ta1 = a1 + s[ci].i;\r\n\t\tb1 = b1 + s[ci].j;\r\n\t\tc1 = c1 + s[ci].m;\r\n\t}\r\n\tfloat w = n[0];\r\n\tint d1 = 0;\r\n\tfor (ci = 0; ci < 5; ci++)\r\n\t{\r\n\t\tif (w < n[ci])\r\n\t\t{\r\n\t\t\tw = n[ci];\r\n\t\t\td1 = ci;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d %s %.1f %.1f %.1f\\n\", s[d1].a, s[d1].x, s[d1].i, s[d1].j, s[d1].m);\r\n\tprintf(\"%.1f %.1f %.1f\", a1 / 5, b1 / 5, c1 / 5);\r\n}"
  },
  "3765": {
    "sid": 2480341,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tstruct er{\r\n\t\tchar f1[16];\r\n\t\tint f2;\r\n\t\tint f3;\r\n\t\tint f4;\r\n\t}s[n];\r\n\tint i;\r\n\tint a,b,c;\r\n\tfloat a1=0,b1=0,c1=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%s%d%d%d\",&s[i].f1,&s[i].f2,&s[i].f3,&s[i].f4);\r\n\t\ta1=a1+s[i].f2;\r\n\t\tb1=b1+s[i].f3;\r\n\t\tc1=c1+s[i].f4;\r\n\t}\r\n\tprintf(\"%.2f %.2f %.2f\",a1/n,b1/n,c1/n);\r\n}\r\n"
  },
  "3078": {
    "sid": 2480340,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[1000]={0},b[100];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&b[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ta[b[i]]++;\r\n\t}\r\n\tint max=0,w=0;\r\n\tfor(i=0;i<1000;i++)\r\n\t{\r\n\t\tif(max<a[i])\r\n\t\tmax=a[i];\r\n\t}\r\n\tif(max==1)\r\n\tprintf(\"NO\");\r\n\telse\r\n\tfor(i=0;i<1000;i++)\r\n\t{\r\n\t\tif(max==a[i])\r\n\t\t{\r\n\t\t\tif(w==0)\r\n\t\t\t{\r\n\t\t\tprintf(\"%d\",i);\r\n\t\t\tw++;\r\n\t    \t}\r\n\t    \telse\r\n\t    \tprintf(\" %d\",i);\r\n\t\t}\r\n\t\t\r\n\t}\r\n}"
  },
  "3079": {
    "sid": 2480339,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[10];\r\n\tint i;\r\n\tint j,m=0;\r\n\tscanf(\"%d\",&a[0]);\r\n\tfor(i=1;i<10;)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t\tm=0;\r\n\t\tfor(j=0;j<i;j++)\r\n\t\t{\r\n\t\t\tif(a[i]==a[j])\r\n\t\t\tm++;\r\n\t\t}\r\n\t\tif(m!=0)\r\n\t\tcontinue;\r\n\t\telse\r\n\t\ti++;\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",a[i]);\r\n\t}\r\n}"
  },
  "3096": {
    "sid": 2480338,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100];\r\n\tint n,i;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++) \r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint b[100];\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tb[i]=a[i]+a[i+1];\r\n\t}\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",b[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",b[i]);\r\n\t}\r\n}"
  },
  "3097": {
    "sid": 2480337,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[100],b[100],c[100];\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\tscanf(\"%d\",&a[i]);\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=0;i<m;i++)\r\n\tscanf(\"%d\",&b[i]);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tc[i]=a[i];\r\n\t}\r\n\tint j; \r\n\tfor(j=0;j<m;j++,i++)\r\n\t{\r\n\t\tc[i]=b[j];\r\n\t}\r\n\tint t;\r\n\tfor(i=0;i<m+n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<m+n-i-1;j++)\r\n\t\t{\r\n\t\t\tif(c[j]<c[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=c[j];\r\n\t\t\t\tc[j]=c[j+1];\r\n\t\t\t\tc[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n+m;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",c[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",c[i]);\r\n\t}\r\n}"
  },
  "3766": {
    "sid": 2480336,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i;\r\n\tscanf(\"%d\",&n);\r\n\tstruct ad{\r\n\t\tchar a[16];\r\n\t\tint b;\r\n\t\tint c;\r\n\t\tint d;\r\n\t}s[n];\r\n\tint a1,b1,c1;\r\n\tint f1=0,f2=0,f3=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\t    scanf(\"%s%d%d%d\",&s[i].a,&s[i].b,&s[i].c,&s[i].d);\r\n\t    \tif(f1<s[i].b)\r\n\t    \t{\r\n\t    \t\tf1=s[i].b;\r\n\t     \t\ta1=i;\r\n\t    \t}\r\n    \t\tif(f2<s[i].c)\r\n    \t\t{\r\n    \t\t\tf2=s[i].c;\r\n     \t\t\tb1=i;\r\n     \t\t}\r\n     \t\tif(f3<s[i].d)\r\n     \t\t{\r\n\t     \t\tf3=s[i].d;\r\n\t      \t\tc1=i;\r\n\t    \t}\r\n\t}\r\n\tprintf(\"%s %d\\n\",s[a1].a,f1);\r\n\tprintf(\"%s %d\\n\",s[b1].a,f2);\r\n\tprintf(\"%s %d\",s[c1].a,f3);\r\n\t\r\n}"
  },
  "3296": {
    "sid": 2480335,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tint c;\r\n\tc=a-b;\r\n\tif(c>=0)\r\n\tc=c;\r\n\telse\r\n\tc=-c;\r\n\tprintf(\"%d\",c);\r\n}"
  },
  "3256": {
    "sid": 2480334,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tif(n==0)\r\n\treturn 0;\r\n\tint i,sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tif(i%2==1)\r\n\t\tsum=((i+1)/2)*((i+1)/2);\r\n\t\tif(i%2==0)\r\n\t\tsum=i/2*(i/2+1);\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "3095": {
    "sid": 2480333,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,i,j,a1,b,c,d,e;\r\n\tscanf(\"%d\",&n);\r\n\tn=n+1;\r\n\tint a[100][100];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<=i+1;j++)\r\n\t\t{\r\n\t\t\ta1=1;\r\n\t    \te=1;\r\n\t\t\tif(j==0||i==0)\r\n\t\t\ta[i][j]=1;\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tfor(c=i,d=0;d<j;d++,c--)\r\n\t\t\t\ta1=a1*c;\r\n\t\t\t\tfor(c=1;c<=j;c++)\r\n\t\t\t\t{\r\n\t\t\t\t\te=e*c;\r\n\t\t\t\t}\r\n\t\t\t\ta[i][j]=a1/e;\r\n\t\t\t}\r\n\t\t\t\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<=i;j++)\r\n\t\t{\r\n\t\t\tif(j==0)\r\n\t\t\tprintf(\"%d\",a[i][j]);\r\n\t\t\telse\r\n\t\t\tprintf(\"  %d\",a[i][j]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "3082": {
    "sid": 2480332,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tfloat a[m][n];\r\n\tint i,j,z;\r\n\tfloat x=0,y=0;\r\n\tfor(i=0,z=0;i<m;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%f\",&a[i][j]);\r\n\t\t}\r\n\t}\r\n\tfloat b[100];\r\n\tfor(j=0;j<n;j++)\r\n\t{\r\n\t\tx=0;\r\n\t\tfor(i=0;i<m;i++)\r\n    \t{\r\n\t\t    x=x+a[i][j];\r\n     \t}\r\n     \tb[j]=x/m;\r\n\t}\r\n\tb[n]=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tb[n]=b[n]+b[i]; \r\n\t}\r\n\tb[n]=b[n]/n;\r\n\tfor(i=0;i<=n;i++)\r\n\t{\r\n\t\tif(i==n)\r\n\t\tprintf(\"%.2f\",b[i]);\r\n\t\telse\r\n\t\tprintf(\"%.2f\\n\",b[i]);\r\n\t\t\r\n\t}\r\n} "
  },
  "3094": {
    "sid": 2480331,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[n][n];\r\n\tint i,j;\r\n\tint sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tif(i==j||i+j==n-1)\r\n\t\t\tcontinue;\r\n\t\t\telse\r\n\t\t\tsum=sum+a[i][j];\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "3649": {
    "sid": 2480330,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tfloat a1=0,b=0,c=0,d=0,a[3][5];\r\n\tint i,j;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<5;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%f\",&a[i][j]);\r\n\t\t} \r\n\t} \r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\ta1=a1+a[0][i];\r\n\t} \r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\tb=b+a[1][i];\r\n\t}\r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\tc=c+a[2][i]; \r\n\t}\r\n\t\r\n\ta1=a1/5;\r\n\tb=b/5;\r\n\tc=c/5;\r\n\td=(a1+b+c)/3;\r\n\tprintf(\"%.2f %.2f %.2f\\n%.2f\",a1,b,c,d);\r\n\t\r\n} "
  },
  "3777": {
    "sid": 2480329,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m=0,n,a[3][4];\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<4;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d,\",&a[i][j]);\r\n\t\t\tif(a[i][j]>0)\r\n\t\t\tm=m+a[i][j];\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",m);\r\n}"
  },
  "3810": {
    "sid": 2480328,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tint a[m][n];\r\n\tint i,j;\r\n\tint b[m];\r\n\tint x=0;\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tx=0;\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tx=x+a[i][j];\r\n\t\t}\r\n\t\tb[i]=x;\r\n\t}\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",b[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",b[i]);\r\n\t}\r\n}"
  },
  "1549": {
    "sid": 2480327,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tchar a[n][100];\r\n\tint i,j;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;a[i][j]!='\\0';j++)\r\n\t\t{\r\n\t\t\tif(a[i][j]==' ')\r\n\t\t\ta[i][j]=',';\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tputs(a[i]);\r\n\t}\r\n}"
  },
  "1907": {
    "sid": 2480326,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[3][3];\r\n\tint i,j;\r\n\tint sum=0;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tfor(j=0;j<3;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tif(i==j)\r\n\t\t\tsum=sum+a[i][j];   \r\n\t\t}\t\t\t        \r\n\t}\r\n\tprintf(\"%d\",sum);\r\n} \r\n "
  },
  "1015": {
    "sid": 2480325,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100][100];\r\n\tint n;\r\n\tint i,j,x;\r\n\tscanf(\"%d\",&n);\r\n\tint c=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0,x=i;j<=i&&x>=0;j++,x--)\r\n\t\t{\r\n\t\t\tc++;\r\n\t\t\ta[x][j]=c;\r\n\t\t}\r\n\t}\r\n\tfor(i=n-1,x=0;i>=0;i--,x++)\r\n\t{\r\n\t\tfor(j=0;j<=i;j++)\r\n\t\t{\r\n\t\t\tif(j==0)\r\n\t\t\tprintf(\"%d\",a[x][j]);\r\n\t\t\telse\r\n\t\t\tprintf(\" %d\",a[x][j]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1800": {
    "sid": 2480323,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tint i;\r\n\tfor(i=0;a[i]!='\\0';i++)\r\n\t{\r\n\t\tif(a[i]>='A'&&a[i]<'Z')\r\n\t\ta[i]=a[i]+33;\r\n\t\telse if(a[i]=='Z')\r\n\t\ta[i]='a';\r\n\t\telse if(a[i]>='a'&&a[i]<='c')\r\n\t\ta[i]='2';\r\n\t\telse if(a[i]>='d'&&a[i]<='f')\r\n\t\ta[i]='3';\r\n\t\telse if(a[i]>='g'&&a[i]<='i')\r\n\t\ta[i]='4';\r\n\t\telse if(a[i]>='j'&&a[i]<='l')\r\n\t\ta[i]='5';\r\n\t\telse if(a[i]>='m'&&a[i]<='o')\r\n\t\ta[i]='6';\r\n\t\telse if(a[i]>='p'&&a[i]<='s')\r\n\t\ta[i]='7';\r\n\t\telse if(a[i]>='t'&&a[i]<='v')\r\n\t\ta[i]='8';\r\n\t\telse if(a[i]>='w'&&a[i]<='z')\r\n\t\ta[i]='9';\r\n\t\telse\r\n\t\ta[i]=a[i];\r\n\t}\r\n\tputs(a);\r\n}"
  },
  "1801": {
    "sid": 2480322,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint gui(float a)\r\n{\r\n\tint a1;\r\n    a1=a*10;\r\n    int b;\r\n    b=(int)a1%10;\r\n    if(b-5<0)\r\n    return (int)a;\r\n    else\r\n\treturn (int)a+1;\r\n}\r\nint main()\r\n{\r\n\tstruct man{\r\n\t\tint a1;\r\n\t\tint a2;\r\n\t\tint a3;\r\n\t\tint a4;\r\n\t\tint a5;\r\n\t\tint a6;\r\n\t\tint a7;\r\n\t\tchar b[30];\r\n\t}s;\r\n\tfloat sum=0;\r\n\tint d;\r\n\tint c=0;\r\n\twhile(~(scanf(\"%d%d%d%d%d%d%d%s\",&s.a1,&s.a2,&s.a3,&s.a4,&s.a5,&s.a6,&s.a7,s.b))&&c<=100)\r\n\t{\r\n\t\tsum=s.a1+s.a2+s.a3+s.a4+s.a5+s.a6+s.a7;\r\n\t\tsum=sum/7;\r\n\t\tprintf(\"%s %.2f\\n\",s.b,(float)gui(sum));\r\n\t\tc++;\r\n\t}\r\n}"
  },
  "1802": {
    "sid": 2480321,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint i=0;\r\n\twhile(~(scanf(\"%d\",&n)))\r\n\t{\r\n\t\tif(n==0)\r\n\t\treturn 0;\r\n\t\ti=0;\r\n\t\twhile(n!=0&&n!=1)\r\n     \t{\r\n\t    \tn=n/2;\r\n\t      \ti++;\r\n    \t}\r\n    \tprintf(\"%d\\n\",i);\r\n\t}\r\n}"
  },
  "1809": {
    "sid": 2480319,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a1[10000];\r\n\tint i;\r\n\tint a=0,b=0,c=0,d=0;\r\n\tint x=0;\r\n\twhile(gets(a1))\r\n\t{\r\n        a=0;\r\n    \tb=0;\r\n   \t\tc=0;\r\n   \t\td=0;\r\n\t\tfor(i=0;a1[i]!='\\0';i++)\r\n    \t{\r\n    \t\tif((a1[i]>='a'&&a1[i]<='z')||(a1[i]>='A'&&a1[i]<='Z'))\r\n    \t\ta++;\r\n\t    \telse if(a1[i]>='0'&&a1[i]<='9')\r\n    \t\tb++;\r\n\t    \telse if(a1[i]==' ')\r\n\t    \tc++;\r\n\t    \telse\r\n\t    \td++;\r\n    \t}\r\n    \tprintf(\"%d %d %d %d\\n\",a,b,c,d);\r\n    \tif(x>=100)\r\n    \treturn 0;\r\n    \tx++;\r\n\t}\r\n}"
  },
  "3075": {
    "sid": 2480318,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tint i1, i, j;\r\n\tfor (i1 = 0; i1 < a[i1] != 0; i1++)\r\n\t{\r\n\t\t;\r\n\t}\r\n\tchar t;\r\n\tint x, y;\r\n\tfor (i = 0; i < i1 - 1; i++)\r\n\t{\r\n\t\tfor (j = 0; j < i1 - 1 - i; j++)\r\n\t\t{\r\n\t\t\tx = a[j];\r\n\t\t\ty = a[j + 1];\r\n\t\t\tif (x > y)\r\n\t\t\t{\r\n\t\t\t\tt = a[j];\r\n\t\t\t\ta[j] = a[j + 1];\r\n\t\t\t\ta[j + 1] = t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tputs(a);\r\n}"
  },
  "3776": {
    "sid": 2480317,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    char a[100], b[100];\r\n    gets(a);\r\n    gets(b);\r\n    int x, y;\r\n    for (x = 0; a[x] != '\\0'; x++)\r\n    {\r\n        ;\r\n    }\r\n    for (y = 0; b[y] != '\\0'; y++)\r\n    {\r\n        if (b[y] >= '0' && b[y] <= '9')\r\n        {\r\n            a[x] = b[y];\r\n            x++;\r\n        }\r\n    }\r\n    a[x] = '\\0';\r\n    puts(a);\r\n}"
  },
  "3089": {
    "sid": 2480316,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\", &n);\r\n\tgetchar();\r\n\tchar a[100][100];\r\n\tint i, j;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tint x = strlen(a[0]);\r\n\tint y = 0;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tif (x < strlen(a[i]))\r\n\t\t{\r\n\t\t\tx = strlen(a[i]);\r\n\t\t\ty = i;\r\n\t\t}\r\n\t}\r\n\tfor (i = 0; a[y][i] != '\\0'; i++)\r\n\t{\r\n\t\tif (a[y][i] >= 'a' && a[y][i] <= 'z')\r\n\t\t\ta[y][i] = a[y][i] - 32;\r\n\t}\r\n\ta[y][i] = '\\0';\r\n\tputs(a[y]);\r\n}"
  },
  "1890": {
    "sid": 2480315,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint i, j, x, y;\r\n\tscanf(\"%d\", &n);\r\n\tfor (x = 1; x <= n; x++)\r\n\t{\r\n\t\tfor (i = n - x; i >= 1; i--)\r\n\t\t\tprintf(\" \");\r\n\t\tfor (j = 1; j <= 2 * x - 1; j++)\r\n\t\t\tprintf(\"*\");\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\tfor (x = 1; x <= n - 1; x++)\r\n\t{\r\n\t\tfor (i = 1; i <= x; i++)\r\n\t\t\tprintf(\" \");\r\n\t\tfor (j = 1; j <= 2 * (n - x) - 1; j++)\r\n\t\t\tprintf(\"*\");\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1012": {
    "sid": 2480313,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint p;\r\n\tscanf(\"%d\",&p);\r\n\tgetchar();\r\n\tchar s[1002];\r\n\twhile(p--)\r\n\t{\r\n\t\tgets(s);\r\n\t\tputs(s);\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\twhile(scanf(\"%s\",s)!=EOF)\r\n\t{\r\n\t\tprintf(\"%s\",s);\r\n\t\tprintf(\"\\n\\n\");\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1013": {
    "sid": 2480312,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint pan(int m)\r\n{\r\n\tint x=0;\r\n\twhile(1)\r\n\t\t{\r\n\t\t\tif(m==1)\r\n\t\t\t{\r\n\t\t\t\tx++;\r\n\t\t\t\treturn x;\r\n\t\t\t}\r\n            else\r\n            {\r\n      \t        x++;\r\n      \t        if(m%2==1)\r\n      \t        m=m*3+1;\r\n      \t        else\r\n      \t        m=m/2;\r\n            }\t\r\n\t\t}\r\n}\r\nint main()\r\n{\r\n\tint c=0;\r\n\tint x,y;\r\n\tint m,n;\r\n\tint a;\r\n\tint i,j;\r\n\twhile(scanf(\"%d%d\",&m,&n)!=EOF)\r\n\t{\r\n\t\tx=m>n?m:n;\r\n\t\ty=m>n?n:m;\r\n\t\ta=pan(y);\r\n\t\tfor(i=y;i<=x;i++)\r\n\t\t{\r\n\t\t\tif(a<pan(i))\r\n\t\t\ta=pan(i);\r\n\t\t}\r\n\t\tprintf(\"%d %d %d\\n\",m,n,a);\r\n\t\tc++;\r\n\t\tif(c>=1000)\r\n\t\tbreak;\r\n\t}\r\n}"
  },
  "1135": {
    "sid": 2480311,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint i, j, x, y;\r\n\tchar m;\r\n\twhile((scanf(\"%c%d\",&m,&n))!=EOF)\r\n\t{\r\n\t\tgetchar();\r\n\t\tfor (x = 1; x <= n; x++)\r\n    \t{\r\n\t    \tfor (i = n - x; i >= 1; i--)\r\n\t\t\tprintf(\" \");\r\n\t    \tfor (j = 1; j <= 2 * x - 1; j++)\r\n\t\t\tprintf(\"%c\",m);\r\n\t    \tprintf(\"\\n\");\r\n    \t}\r\n    \tfor (x = 1; x <= n - 1; x++)\r\n    \t{\r\n     \t\tfor (i = 1; i <= x; i++)\r\n   \t\t\tprintf(\" \");\r\n    \t\tfor (j = 1; j <= 2 * (n - x) - 1; j++)\r\n\t\t\tprintf(\"%c\",m);\r\n    \t\tprintf(\"\\n\");\r\n    \t}\r\n\t}\r\n}\r\n"
  },
  "1136": {
    "sid": 2480310,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint jie(int a)\r\n{\r\n\tif(a==1)\r\n\treturn 1;\r\n\telse\r\n\treturn jie(a-1)*a;\r\n} \r\nint he(int n)\r\n{\r\n\tint i;\r\n\tint sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+jie(i);\r\n\t}\r\n\treturn sum;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(~(scanf(\"%d\",&n)))\r\n\t{\r\n\t\tprintf(\"%d\\n\",he(n));\r\n\t} \r\n\t\r\n} "
  },
  "1137": {
    "sid": 2480309,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nfloat sum(int a,float b)\r\n{\r\n\tint i;\r\n\tfloat s=0;\r\n\tfor(i=0;i<=a;i++)\r\n\t{\r\n\t\ts=s+pow(b,i);\r\n\t}\r\n\treturn s;\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tfloat b;\r\n\twhile(scanf(\"%d%f\",&a,&b)!=EOF)\r\n\t{\r\n\t\tprintf(\"%.3f\\n\",sum(a,b));\r\n\t}\r\n}"
  },
  "1822": {
    "sid": 2480308,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nvoid pai(char a[])\r\n{\r\n\tint i,j;\r\n\tchar t;\r\n\tfor(i=0;i<strlen(a)-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<strlen(a)-1-i;j++)\r\n\t\t{\r\n\t\t\tif((int)a[j]>(int)a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%c\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %c\",a[i]);\r\n\t}\r\n\t\r\n}\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tint i;\r\n\twhile(gets(a))\r\n\t{\r\n\t\tpai(a);\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "3048": {
    "sid": 2480307,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tint sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tif(i%3==0)\r\n\t\tsum=sum+i;\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n} "
  },
  "3047": {
    "sid": 2480306,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse\r\n\treturn fac(n-1)*n; \r\n}\r\nint sum(int n)\r\n{\r\n\tint i;\r\n\tint x=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tif(i%2==1)\r\n\t\tx=x+fac(i);\r\n\t\telse\r\n\t\tx=x-fac(i);\r\n\t}\r\n\treturn x;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tprintf(\"%d\",sum(n));\r\n}"
  },
  "3771": {
    "sid": 2480304,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n   struct time{\r\n\t\tint year;\r\n\t\tint month;\r\n\t\tint day;\r\n\t\tint h;\r\n\t\tint min;\r\n\t\tint s;\r\n\t}s[3];\r\n\tint i;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tscanf(\"%d %d %d %d %d %d\",&s[i].year,&s[i].month,&s[i].day,&s[i].h,&s[i].min,&s[i].s);\r\n\t}\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tprintf(\"%d/%02d/%.2d %02d:%02d:%02d\\n\",s[i].year,s[i].month,s[i].day,s[i].h,s[i].min,s[i].s);\r\n\t}\r\n}"
  },
  "3085": {
    "sid": 2480303,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tchar a[100];\r\n\tgets(a);\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n}"
  },
  "2902": {
    "sid": 2480301,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tint c;\r\n\twhile(~(scanf(\"%d%d\",&a,&b)))\r\n\t{\r\n\t\tif(a>=1&&b<=pow(10,9))\r\n\t\tc=a+b;\r\n\t\tprintf(\"%d\\n\",c);\r\n\t}\r\n}"
  },
  "2904": {
    "sid": 2480299,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\twhile(~(scanf(\"%d%d\",&a,&b)))\r\n\t{\r\n\t\tif(a>0&&b<=pow(2,10))\r\n\t\t{\r\n\t\t\tc=a*b;\r\n\t\t\tc=c%10;\r\n\t\t\tprintf(\"%d\\n\",c);\r\n\t\t}\r\n\t}\r\n}"
  },
  "2916": {
    "sid": 2480298,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint fac(int *p)\r\n{\r\n\tint i;\r\n\tint y;\r\n\ty=*p;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(y>*(p+i))\r\n\t\t{\r\n\t\t\ty=*(p+i);\r\n\t\t}\r\n\t}\r\n\treturn y;\r\n}\r\nint main()\r\n{\r\n\tint a[10];\r\n\tint i;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tprintf(\"%d\",fac(a));\r\n}"
  },
  "2915": {
    "sid": 2480297,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c,d,e;\r\n\tfloat f;\r\n\tscanf(\"%d%d%d%d%d\",&a,&b,&c,&d,&e);\r\n\tf=a+b+c+d+e;\r\n\tf=f/5;\r\n\tprintf(\"%.2f\",f);\r\n}"
  },
  "3830": {
    "sid": 2480296,
    "code": "C++",
    "content": " #include <stdio.h>\n #include <stdio.h>\n#include <stdio.h> \r\nstruct Student{\r\n\tchar name[16];\r\n\tdouble m;\r\n\tdouble e;\r\n};\r\nint main()          \r\n{\r\n   struct  Student  t[3];\r\n    int i=0;\r\n    while(i<3)       \r\n    {\r\n        scanf(\"%s\", t[i].name);\r\n        scanf(\"%lf\", &t[i].m);\r\n        scanf(\"%lf\", &t[i].e);\r\n               i++;\r\n    }\r\n    i=0;\r\n    double sum=0;\r\n   for(i=0;i<3;i++)\r\n    {\r\n    \tsum=0;\r\n    \tsum=t[i].m+t[i].e;\r\n    \tif(sum/2>=60)\r\n    \t{\r\n  \t\t\tprintf(\"%s\",t[i].name);\r\n  \t\t\treturn 0;\r\n\t    }\r\n    }\r\n}  "
  },
  "1837": {
    "sid": 2480295,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\t char a[100];\r\n\t int i;\r\n\t int b=0;\r\n     while(gets(a))\r\n     {\r\n     \tif(a[0]>='a'&&a[0]<='z')\r\n         {\r\n  \t\t \ta[0]=a[0]-32; \r\n         }\r\n    \t for(i=1;i<strlen(a);i++)\r\n    \t {\r\n \t    \tif((a[i]>='a'&&a[i]<='z')&&a[i-1]==' ')\r\n     \t\t{\r\n\t\t    \ta[i]=a[i]-32;\r\n\t        }\r\n     \t }\r\n   \t     puts(a);\r\n   \t     b++;\r\n   \t     if(b>=50)\r\n   \t     return 0;\r\n     }\r\n\t \r\n}"
  },
  "1909": {
    "sid": 2480294,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nvoid fac(char a[])\r\n{\r\n\tint i;\r\n\tfor(i=strlen(a)-1;i>=0;i--)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tchar a[100];\r\n    int i;\r\n    gets(a);\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tif(a[i]>='a'&&a[i]<='z')\r\n\t\ta[i]=a[i]-32;\r\n\t\telse if(a[i]>='A'&&a[i]<='Z')\r\n\t\ta[i]=a[i]+32;\r\n\t\telse if(a[i]>='0'&&a[i]<='9')\r\n\t\t{\r\n\t\t\tswitch(a[i])\r\n\t\t\t{\r\n\t\t\t\tcase '0':a[i]='9';break;\r\n\t     \t   \tcase '1':a[i]='8';break;\r\n\t     \t\tcase '2':a[i]='7';break;\r\n\t     \t\tcase '3':a[i]='6';break;\r\n\t\t    \tcase '4':a[i]='5';break;\r\n\t\t    \tcase '5':a[i]='4';break;\r\n\t     \t\tcase '6':a[i]='3';break;\r\n\t\t    \tcase '7':a[i]='2';break;\r\n\t\t    \tcase '8':a[i]='1';break;\r\n\t\t    \tcase '9':a[i]='0';\r\n\t\t\t}\r\n\t\t\t\r\n\t\t}\r\n\t}\t\r\n    fac(a);\r\n}"
  },
  "1140": {
    "sid": 2480293,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    int a, b, u, v, r, m;\r\n    while (scanf(\"%d%d\", &a, &b) != EOF)\r\n    {\r\n        u = a;\r\n        v = b;\r\n        while (v != 0)\r\n        {\r\n            r = u % v;\r\n            u = v;\r\n            v = r;\r\n        }\r\n        m = a / u * b;\r\n        printf(\"%d\\n\", m);\r\n    }\r\n}"
  },
  "1139": {
    "sid": 2480292,
    "code": "C++",
    "content": "#define _CRT_SECURE_NO_WARNINGS\r\n#include<stdio.h>\r\nint main()\r\n{\r\n    int a, b, u, v, r, m;\r\n    while (scanf(\"%d%d\", &a, &b) != EOF)\r\n    {\r\n        u = a;\r\n        v = b;\r\n        while (v != 0)\r\n        {\r\n            r = u % v;\r\n            u = v;\r\n            v = r;\r\n        }\r\n        printf(\"%d\\n\", u);\r\n    }\r\n}"
  },
  "1917": {
    "sid": 2480291,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i,j,m,n,x;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tfor(j=2*(n-i);j>=1;j--)\r\n\t\t{\r\n\t\t\tprintf(\" \");\r\n\t\t}\r\n\t\tfor(m=1;m<=i;m++)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",m);\r\n\t\t\tif(i!=1)\r\n\t\t\tprintf(\" \"); \r\n\t\t}\r\n\t\tfor(x=i-1;x>0;x--)\r\n\t\t{\r\n\t\t\tprintf(\"%d\",x);\r\n\t\t    if(x!=1)\r\n\t\t    printf(\" \");\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "4235": {
    "sid": 2480290,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\", &n);\r\n\tint m, x;\r\n\tm = n / 8;\r\n\tm = m * 2;\r\n\tx = n % 8;\r\n\tif (x >= 1)\r\n\t\tm = m + 1;\r\n\tfloat a;\r\n\ta = 98.88 / m;\r\n\tint b;\r\n\tb = a;\r\n\tfloat c;\r\n\tc = b + 0.88;\r\n\twhile (c <a)\r\n\t{\r\n\t\tc++;\r\n\t}\r\n\tprintf(\"%.2f\", c);\r\n}"
  },
  "1141": {
    "sid": 2480289,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tfloat sum=0;\r\n\tint a;\r\n\tint i;\r\n\tint b=0;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t\tsum=0;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a);\r\n\t\t\tsum=sum+a;\r\n\t\t}\r\n\t\tsum=sum/n;\r\n\t\tprintf(\"%.3f\\n\",sum);\r\n\t\tb++;\r\n\t\tif(b>=5)\r\n\t\tbreak;\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1146": {
    "sid": 2480288,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#include<string.h>\r\nusing namespace std;\r\nint main()\r\n{\r\n    int n, i, j = 0;\r\n    char a[51];\r\n    scanf(\"%d\", &n);\r\n    while (n--)\r\n    {\r\n        j++;\r\n        scanf(\"%s\", &a);\r\n        for (i = 0; i < strlen(a); i++)\r\n        {\r\n            if (a[i] == 'Z')\r\n                a[i] = 'A';\r\n            else\r\n                a[i] += 1;\r\n        }\r\n        printf(\"String #%d\\n\", j);\r\n        for (i = 0; i < strlen(a); i++)\r\n        {\r\n            printf(\"%c\", a[i]);\r\n        }\r\n        printf(\"\\n\\n\");\r\n    }\r\n    return 0;\r\n}\r\n"
  },
  "1877": {
    "sid": 2480286,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"******************************\\n\\n\");\r\n\tprintf(\"          Very good!\\n\\n\");\r\n    printf(\"******************************\");\r\n}"
  },
  "1548": {
    "sid": 2480285,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tstruct time{\r\n\t\tint year;\r\n\t\tint month;\r\n\t\tint day;\r\n\t}s;\r\n\tscanf(\"%d%d%d\",&s.year,&s.month,&s.day);\r\n\tint sum=0;\r\n\tswitch(s.month)\r\n\t{\r\n\t\tcase 12:sum=sum+30;\r\n\t\tcase 11:sum=sum+31;\r\n\t\tcase 10:sum=sum+30;\r\n\t\tcase 9:sum=sum+31;\r\n\t\tcase 8:sum=sum+31;\r\n\t\tcase 7:sum=sum+30;\r\n\t\tcase 6:sum=sum+31;\r\n\t\tcase 5:sum=sum+30;\r\n\t\tcase 4:sum=sum+31;\r\n\t\tcase 3:sum=sum+28;\r\n\t\tcase 2:sum=sum+31;\r\n\t\tcase 1:sum=sum+s.day;\r\n\t}\r\n\tif(s.month>=3&&(s.year%4==0&&s.year%100!=0||s.year%400==0))\r\n\tsum++;\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "1891": {
    "sid": 2480284,
    "code": "C++",
    "content": "#include<stdio.h>\r\ndouble fac(double n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse if(n==2)\r\n\treturn 2;\r\n\telse\r\n\treturn fac(n-1)+fac(n-2);\r\n}\r\nint main()\r\n{\r\n\tdouble i;\r\n\tdouble sum=0;\r\n\tdouble n;\r\n\tscanf(\"%lf\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+(fac(i+1)/fac(i));\r\n\t}\r\n\tprintf(\"%.6f\",sum);\r\n}"
  },
  "1803": {
    "sid": 2480283,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar s1[100000],s2[100000];\r\n\tint x,y;\r\n\tint i,j;\r\n\twhile(scanf(\"%s %s\",&s1,&s2)!=EOF)\r\n\t{\r\n\t\tx=strlen(s1);\r\n\t\ty=strlen(s2);\r\n\t\tif(s1[0]=='0'&&s2[0]=='0'&&x==1&&y==1)\r\n\t\tbreak;\r\n\t\tif(x>=y)\r\n\t\t{\r\n\t \t\tfor(i=0,j=0;i<x;i++)\r\n\t\t\t{\r\n\t\t\t\tif(s1[i]+s2[j]=='A'+'Z')\r\n\t\t\t\tj++;\r\n\t\t\t}\r\n    \t\tif(j==y)\r\n \t        printf(\"Yes\\n\");\r\n \t   \t    else\r\n\t\t\tprintf(\"No\\n\");\r\n\t\t}\r\n\t\telse\r\n\t\tprintf(\"No\\n\");\r\n\t\t\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1806": {
    "sid": 2480282,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100][100];\r\n\tint n;\r\n\tint i,j;\r\n\twhile(scanf(\"%d\",&n))\r\n\t{\r\n\t\tif(n==0)\r\n\t\t{\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tfor(j=0;j<=i;j++)\r\n\t\t\t{\r\n\t\t\t\tif(j==0||j==i)\r\n\t\t\t\t{\r\n\t\t\t\t\ta[i][j]=1;\r\n\t\t\t\t\tcontinue;\r\n\t\t\t\t}\r\n\t\t\t\telse\r\n\t\t\t\ta[i][j]=a[i-1][j]+a[i-1][j-1];\r\n\t\t\t}\r\n\t\t}\t\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tfor(j=0;j<=i;j++)\r\n\t\t\t{\r\n\t\t\t\tif(j==0)\r\n\t\t\t\tprintf(\"%d\",a[i][j]);\r\n\t\t\t\telse\r\n\t\t\t\tprintf(\" %d\",a[i][j]);\r\n\t\t\t}\r\n\t\t\tprintf(\"\\n\");\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "3877": {
    "sid": 2480281,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100][100];\r\n\tint n;\r\n\tint i,j;\r\n\tscanf(\"%d\",&n);\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tfor(j=0;j<=i;j++)\r\n\t\t\t{\r\n\t\t\t\tif(j==0||j==i)\r\n\t\t\t\t{\r\n\t\t\t\t\ta[i][j]=1;\r\n\t\t\t\t\tcontinue;\r\n\t\t\t\t}\r\n\t\t\t\telse\r\n\t\t\t\ta[i][j]=a[i-1][j]+a[i-1][j-1];\r\n\t\t\t}\r\n\t\t}\t\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<=i;j++)\r\n\t\t{\r\n\t\t\tprintf(\"%d \",a[i][j]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1543": {
    "sid": 2480279,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[3][100];\r\n\tint i;\r\n\tint c;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t\ta[i][strlen(a[i])]='\\0';\r\n\t}\r\n\tint j;\r\n\tchar b[100];\r\n\tfor(i=0;i<2;i++)\r\n\t{\r\n\t\tfor(j=0;j<2-i;j++)\r\n\t\t{\r\n\t\t\tif(strcmp(a[j],a[j+1])>0)\r\n\t\t\t{\r\n\t\t\t\tstrcpy(b,a[j]);\r\n\t\t\t\tstrcpy(a[j],a[j+1]);\r\n\t\t\t    strcpy(a[j+1],b);\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tputs(a[i]);\r\n\t}\r\n}"
  },
  "1147": {
    "sid": 2480278,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\", &n);\r\n\tint i;\r\n\tint m;\r\n\tint b[100];\r\n\tint j;\r\n\tint x, y, z, f, e, g;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tscanf(\"%d\", &m);\r\n\t\tx = 0;\r\n\t\twhile (m != 0)\r\n\t\t{\r\n\t\t\tj = m % 2;\r\n\t\t\tb[x] = j;\r\n\t\t\tm = m / 2;\r\n\t\t\tx++;\r\n\t\t}\r\n\t\te = 0;\r\n\t\tfor (f = 0; f < x; f++)\r\n\t\t{\r\n\t\t\tif (b[f] == 1)\r\n\t\t\t{\r\n\t\t\t\tif (e == 0)\r\n\t\t\t\t\tprintf(\"%d\", f);\r\n\t\t\t\telse\r\n\t\t\t\t\tprintf(\" %d\", f);\r\n\t\t\t\t\te++;\r\n\t\t\t}\r\n\t\t}\r\n\t\tif(i!=n-1)\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "3086": {
    "sid": 2480277,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tgets(a);\r\n\tint i;\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tif(a[i]>='a'&&a[i]<='z')\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n}"
  },
  "3087": {
    "sid": 2480276,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint j;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tchar a[100][1000];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tint b;\r\n\tb=strlen(a[0]);\r\n\tint c=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(b<strlen(a[i]))\r\n\t\t{\r\n\t\t\tb=strlen(a[i]);\r\n\t\t\tc=i;\r\n\t\t}\r\n\t}\r\n\tputs(a[c]);\r\n}"
  },
  "3090": {
    "sid": 2480275,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tint i,j;\r\n\tchar a[100][100];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tchar b[10000];\r\n\tint c=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<strlen(a[i]);j++)\r\n\t\t{\r\n\t\t\tb[c]=a[i][j];\r\n\t\t\tc++;\r\n\t\t}\r\n\t}\r\n\tputs(b);\r\n}"
  },
  "3091": {
    "sid": 2480274,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tint i;\r\n\tchar a[100][100];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",strlen(a[i]));\r\n\t\telse\r\n\t\tprintf(\" %d\",strlen(a[i]));\r\n\t}\r\n}"
  },
  "1866": {
    "sid": 2480273,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i,j,m;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tfor(j=1;j<=n-i;j++)\r\n\t\tprintf(\" \");\r\n\t\tfor(m=1;m<=i*2-1;m++)\r\n\t\t{\r\n\t\t\tif(m==1||m==2*i-1)\r\n\t\t\tprintf(\"+\");\r\n\t\t\telse\r\n\t\t\tprintf(\"*\");\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\tfor(i=1;i<n;i++)\r\n\t{\r\n\t\tfor(j=1;j<=i;j++)\r\n\t\tprintf(\" \");\r\n\t\tfor(m=2*(n-i)-1;m>=1;m--)\r\n\t\t{\r\n\t\t\tif(m==1||m==2*(n-i)-1)\r\n\t\t\tprintf(\"+\");\r\n\t\t\telse\r\n\t\t\tprintf(\"*\");\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1148": {
    "sid": 2480272,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tchar a[100];\r\n\tint i,j;\r\n\tint x=1;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a);\r\n\t\ta[strlen(a)]=='\\0';\r\n\t\tx=1;\r\n\t\tfor(j=1;j<=strlen(a);j++)\r\n\t\t{\r\n\t\t\tif(a[j]==a[j-1])\r\n\t\t\t{\r\n\t\t\t\tx++;\r\n\t\t\t\tcontinue;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tif(x==1)\r\n\t\t\t\tprintf(\"%c\",a[j-1]);\r\n\t\t\t\telse\r\n\t\t\t\tprintf(\"%d%c\",x,a[j-1]);\r\n\t\t\t\tx=1;\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1149": {
    "sid": 2480271,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tchar a[10000];\r\n\tint i,j;\r\n\tint x=1;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a);\r\n\t\ta[strlen(a)]=='\\0';\r\n\t\tx=1;\r\n\t\tfor(j=1;j<=strlen(a);j++)\r\n\t\t{\r\n\t\t\tif(a[j]==a[j-1])\r\n\t\t\t{\r\n\t\t\t\tx++;\r\n\t\t\t\tcontinue;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%d%c\",x,a[j-1]);\r\n\t\t\t\tx=1;\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "1150": {
    "sid": 2480270,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint x,y;\r\n\tchar a[100];\r\n\tchar b[100]\t;\r\n\tchar c[100];\r\n\tint j;\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&x);\r\n\t\tfor(j=0;j<x;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%s\",&a);\r\n\t\t\tb[j]=a[0];\r\n\t\t}\r\n\t\tb[j]='\\0';\r\n\t\tscanf(\"%d\",&y);\r\n\t\tfor(j=0;j<y;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%s\",&a);\r\n\t\t\tc[j]=a[0];\r\n\t\t}\r\n\t\tc[j]='\\0';\r\n\t\tif(strcmp(b,c)==0)\r\n\t\tprintf(\"SAME\\n\");\r\n\t\telse\r\n\t\tprintf(\"DIFFERENT\\n\");\r\n\t}\r\n}"
  },
  "1151": {
    "sid": 2480269,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tint i,j;\r\n\tchar a[10000];\r\n\twhile(gets(a))\r\n\t{\r\n\t\ta[strlen(a)]='\\0';\r\n\t\tif(strlen(a)==1&&a[0]=='#')\r\n\t\tbreak;\r\n\t\tfor(i=0;i<strlen(a);i++)\r\n\t\t{\r\n\t\t\tif(a[i]==' ')\r\n\t\t\tprintf(\"%%20\");\r\n\t\t\telse if(a[i]=='!')\r\n\t\t\tprintf(\"%%21\");\r\n\t\t\telse if(a[i]=='$')\r\n\t\t\tprintf(\"%%24\");\r\n\t\t\telse if(a[i]=='%')\r\n\t\t\tprintf(\"%%25\");\r\n\t\t\telse if(a[i]=='(')\r\n\t\t\tprintf(\"%%28\");\r\n\t\t\telse if(a[i]==')')\r\n\t\t\tprintf(\"%%29\");\r\n\t\t\telse if(a[i]=='*')\r\n\t\t\tprintf(\"%%2a\");\r\n\t\t\telse\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1152": {
    "sid": 2480268,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tint b[100];\r\n\tint j;\r\n\tint sum;\r\n\tint i;\r\n\tint n=0;\r\n\twhile (scanf(\"%s\", &a))\r\n\t{\r\n\t\tif (a[0] == '0' && strlen(a) == 1)\r\n\t\tbreak;\r\n\t\tn = 0;\r\n\t\tfor (i = 0; i < strlen(a); i++)\r\n\t\t{\r\n\t\t\tn += a[i] - '0';\r\n\t\t}\r\n\t\tsum = n;\r\n\t\twhile (sum >= 10)\r\n\t\t{\r\n\t\t\tj = 0;\r\n\t\t\twhile (sum != 0)\r\n\t\t\t{\r\n\t\t\t\tb[j] = sum % 10;\r\n\t\t\t\tsum = sum / 10;\r\n\t\t\t\tj++;\r\n\t\t\t}\r\n\t\t\tsum = 0;\r\n\t\t\tfor (i = 0; i < j; i++)\r\n\t\t\t{\r\n\t\t\t\tsum = sum + b[i];\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"%d\\n\", sum);\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1881": {
    "sid": 2480267,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d%d\",&a,&b);\r\n\t\tprintf(\"%d\\n\",a>b?a:b);\r\n\t}\r\n}"
  },
  "1867": {
    "sid": 2480266,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint pan(int n)\r\n{\r\n\tint i,x;\r\n\tx=sqrt(n);\r\n\tfor(i=2;i<=x;i++)\r\n\t{\r\n\t\tif(n%i==0)\r\n\t\treturn 0;\r\n\t}\r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tint i,j;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=2;i<n;i++)\r\n\t{\r\n\t\ta=n-i;\r\n\t\tif(pan(i)==1&&pan(a)==1&&i%2==1)\r\n\t\t{\r\n\t\t\tprintf(\"%d=%d+%d\",n,i,a);\r\n\t\t\tbreak;\r\n\t\t}\t\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1805": {
    "sid": 2480265,
    "code": "C++",
    "content": "#include<stdio.h>.\r\nint main()\r\n{\r\n\tint m, n;\r\n\tint a, b;\r\n\tint i, j = 0;\r\n\tfloat min, max;\r\n\tscanf(\"%d%d\", &m, &n);\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tscanf(\"%d%d\", &a, &b);\r\n\t\tif (a <= 0)\r\n\t\t{\r\n\t\t\tif (j == 0)\r\n\t\t\t\tmin = (m * 1000 - a) / b;\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tmax = (m * 1000 - a) / b;\r\n\t\t\t\tif (min > max)\r\n\t\t\t\t\tmin = max;\r\n\t\t\t}\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%.0f\", min);\r\n}"
  },
  "1153": {
    "sid": 2480264,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint i;\r\n\tint a[10000];\r\n\tint sum;\r\n\tint tem;\r\n\tint j=1;\r\n\twhile(scanf(\"%d\",&n))\r\n\t{\r\n\t\tif(n==0)\r\n\t\tbreak;\r\n\t\tsum=0;\r\n\t\ttem=0;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i]);\r\n\t\t}\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tsum=sum+a[i];\r\n\t\t}\r\n\t\tsum=sum/n;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tif(a[i]<sum)\r\n\t\t\t{\r\n\t\t\t\ttem=tem+(sum-a[i]);\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"Set #%d\\n\",j);\r\n\t\tprintf(\"The minimum number of moves is %d.\\n\",tem);\r\n\t\tprintf(\"\\n\");\r\n\t\tj++;\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1154": {
    "sid": 2480263,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tint j=0;\r\n\tfloat t;\r\n\twhile(scanf(\"%d%d%d\",&a,&b,&c)!=EOF)\r\n\t{\r\n\t\tif(a==0&&b==0&&c==0)\r\n\t\tbreak;\r\n\t\tj++;\r\n\t\tprintf(\"Triangle #%d\\n\",j);\r\n\t\tif(a==-1)\r\n\t\t{\r\n\t\t\tt=sqrt(c*c-b*b);\r\n\t\t\tif(t+b>c&&t>c-t)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"a = %.3f\\n\\n\",t);\r\n\t\t\t}\t\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\"Impossible.\\n\\n\");\r\n\t\t\t}\t\t\t\r\n\t\t}\r\n\t\telse if(b==-1)\r\n\t\t{\r\n\t\t\tt=sqrt(c*c-a*a);\r\n\t\t\tif(t+a>c&&t>c-a)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"b = %.3f\\n\\n\",t);\r\n\t\t\t}\t\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\"Impossible.\\n\\n\");\t\t\t\t\r\n\t\t\t}\t\t\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\t\tt=sqrt(b*b+a*a);\r\n\t\t\t\tprintf(\"c = %.3f\\n\\n\",t);\r\n\t\t}\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1155": {
    "sid": 2480262,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nvoid fac(char *p)\r\n{\r\n\tint i;\r\n\tfor(i=strlen(p)-1;i>=0;i--)\r\n\t{\r\n\t\tprintf(\"%c\",*(p+i));\r\n\t} \r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tint i;\r\n\tchar a[100];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a);\r\n\t\tfac(a);\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "4233": {
    "sid": 2480261,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\n#define pi 3.14\r\nint main()\r\n{\r\n\tfloat n;\r\n\tscanf(\"%f\",&n);\r\n\tfloat s;\r\n\ts=(n*n)/(4*pi);\r\n\tprintf(\"%.1f\",s);\r\n}"
  },
  "4232": {
    "sid": 2480260,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"International Collegiate Programming Contest(\u56fd\u9645\u5927\u5b66\u751f\u7a0b\u5e8f\u8bbe\u8ba1\u7ade\u8d5b),\u662f\u7531\u56fd\u9645\u8ba1\u7b97\u673a\u534f\u4f1a\u4e3b\u529e\u7684,\u4e00\u9879\u65e8\u5728\u5c55\u793a\u5927\u5b66\u751f\u521b\u65b0,\u5206\u6790\u548c\u89e3\u51b3\u95ee\u9898\u80fd\u529b\u7684\u5e74\u5ea6\u7ade\u8d5b.\");\r\n}"
  },
  "4234": {
    "sid": 2480259,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint n, k;\r\n\tscanf(\"%d%d\", &n, &k);\r\n\tint i;\r\n\tfloat sum = 3;\r\n\tfloat a, b;\r\n\ta = n * pow((1.0 / 3.0), k);\r\n\tb = 3 * pow(4, k);\r\n\tsum = a * b;\r\n\tprintf(\"%.2f\", sum);\r\n}"
  },
  "4238": {
    "sid": 2480258,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&n,&m);\r\n\tint a[10000];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint x=1,y=1;\r\n\tint sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]==1)\r\n\t\t{\r\n\t\t\twhile(x)\r\n\t\t\t{\r\n\t\t\t\tsum++;\r\n\t\t\t\tx--;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse if(a[i]==5)\r\n\t\t{\r\n\t\t\twhile(y)\r\n\t\t\t{\r\n\t\t\t\tsum++;\r\n\t\t\t\ty--;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse if(a[i]>=2&&a[i]<=4) \r\n\t\tsum++;\r\n\t}\r\n\tif(x==1)\r\n\tsum--;\r\n\tif(y==1)\r\n\tsum--;\r\n\tif(sum>=m)\r\n\tsum=m;\r\n\tprintf(\"%d\",m-sum);\r\n}"
  },
  "1156": {
    "sid": 2480257,
    "code": "C++",
    "content": "#include <stdio.h>\r\n#define MAXSTACK 1024\r\nchar stack[MAXSTACK];\r\nint pstack;\r\nvoid push(char c)\r\n{\r\n    stack[pstack++] = c;\r\n}\r\nchar pop()\r\n{\r\n    return stack[--pstack];\r\n}\r\nint main(void)\r\n{\r\n    int t, line, i;\r\n    char c;\r\n        scanf(\"%d\", &line);\r\n        getchar();\r\n        pstack = 0;\r\n\r\n        for (i = 1; i <= line; i++)\r\n        {\r\n            c = getchar();\r\n            while (c != '\\n')\r\n            {\r\n                if (c == ' ')\r\n                {\r\n                    while (pstack)\r\n                        putchar(pop());\r\n                    putchar(c);\r\n                }\r\n                else\r\n                    push(c);\r\n                c = getchar();\r\n            }\r\n\r\n            while (pstack)\r\n                putchar(pop());\r\n            if(i!=line)\r\n            putchar('\\n');\r\n        }\r\n    return 0;\r\n}"
  },
  "4237": {
    "sid": 2480255,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i,j,m;\r\n\tfor(i=0;i<=(n/7)+1;i++)\r\n\t{\r\n\t\tfor(j=0;j<=(n/5)+1;j++)\r\n\t\t{\r\n\t\t\tm=(n-7*i-5*j)/3;\r\n\t\t\tif((n-7*i-5*j)%3==0)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%d %d %d\",m,j,i);\r\n\t\t\t\treturn 0;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
  },
  "2403": {
    "sid": 2480253,
    "code": "C++",
    "content": "#include<iostream>\r\n#include<cstdio>\r\n#include<cstring>\r\n#include<algorithm> \r\nusing namespace std;\r\nint a[100010];\r\n\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n),n)\r\n\t{\r\n\t\tint i,sum=0;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t\tsort(a,a+n);\r\n\t\tfor(i=0;i<n-1;i++)\r\n\t\tsum+=a[i+1]-a[i];\r\n\t\tsum+=a[n-1]-a[0];\r\n\t\tprintf(\"%d\\n\",sum);\t \r\n\t}\r\n}"
  },
  "4223": {
    "sid": 2480252,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n, t1, t2, k, m;\r\n\tscanf(\"%d%d%d%d%d\", &n, &t1, &t2, &k, &m);\r\n\tint i, j;\r\n\tfor (i = 1; i <= m; i++)\r\n\t{\r\n\t\tif (i % t1 == 0)\r\n\t\t\tn = n * 2;\r\n\t\tif (i % t2 == 0)\r\n\t\t\tn = n - k;\r\n\t}\r\n\tif (n <= 0)\r\n\t\tn = 0;\r\n\tprintf(\"%d\", n);\r\n}"
  },
  "1884": {
    "sid": 2480251,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tint x,y,z;\r\n\tint i,j,m;\r\n\tscanf(\"%d:%d:%d\",&a,&b,&c);\r\n\tscanf(\"%d:%d:%d\",&x,&y,&z);\r\n\tif(a>x)\r\n\t{\r\n\t\tif(c>=z)\r\n\t\t{\r\n\t\t\tm=c-z;\r\n\t\t\tif(b>=y)\r\n\t\t\t{\r\n\t\t\t\tj=b-y;\r\n\t\t\t\ti=a-x;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-y+b;\r\n\t\t\t\ta--;\r\n\t\t\t\ti=a-x;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tm=60-z+c;\r\n\t\t\tb--;\r\n\t\t\tif(b>=y)\r\n\t\t\t{\r\n\t\t\t\tj=b-y;\r\n\t\t\t\ti=a-x;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-y+b;\r\n\t\t\t\ta--;\r\n\t\t\t\ti=a-x;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\telse if(a==x)\r\n\t{\r\n\t\ti=0;\r\n\t\tif(c>=z)\r\n\t\t{\r\n\t\t\tm=c-z;\r\n\t\t\tif(b>=y)\r\n\t\t\t{\r\n\t\t\t\tj=b-y;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-y+b;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tm=60-z+c;\r\n\t\t\tb--;\r\n\t\t\tif(b>=y)\r\n\t\t\t{\r\n\t\t\t\tj=b-y;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-y+b;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\telse\r\n\t{\r\n\t\tif(z>=c)\r\n\t\t{\r\n\t\t\tm=z-c;\r\n\t\t\tif(y>=b)\r\n\t\t\t{\r\n\t\t\t\tj=y-b;\r\n\t\t\t\ti=x-a;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-b+y;\r\n\t\t\t\tx--;\r\n\t\t\t\ti=x-a;\r\n\t\t\t}\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tm=60-c+z;\r\n\t\t\tb--;\r\n\t\t\tif(y>=b)\r\n\t\t\t{\r\n\t\t\t\tj=y-b;\r\n\t\t\t\ti=x-a;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tj=60-b+y;\r\n\t\t\t\tx--;\r\n\t\t\t\ti=x-a;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%02d:%02d:%02d\",i,j,m);\r\n}"
  },
  "1920": {
    "sid": 2480250,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m, n;\r\n\tint f=0;\r\n\tscanf(\"%d%d\", &n, &m);\r\n\tint a[100][100];\r\n\tint i, j;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tfor (j = 0; j < m; j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\", &a[i][j]);\r\n\t\t}\r\n\t}\r\n\tint x, y;\r\n\tint b[100];\r\n\tint c[100];\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tx = a[i][0];\r\n\t\ty = 0;\r\n\t\tfor (j = 0; j < m; j++)\r\n\t\t{\r\n\t\t\tif (x < a[i][j])\r\n\t\t\t{\r\n\t\t\t\tx = a[i][j];\r\n\t\t\t\ty = j;\r\n\t\t\t}\r\n\t\t}\r\n\t\tb[i] = y;\r\n\t}\r\n\tfor (j = 0; j < n; j++)\r\n\t{\r\n\t\tx = a[0][j];\r\n\t\ty = 0;\r\n\t\tfor (i = 0; i < n; i++)\r\n\t\t{\r\n\t\t\tif (x > a[i][j])\r\n\t\t\t{\r\n\t\t\t\tx = a[i][j];\r\n\t\t\t\ty = i;\r\n\t\t\t}\r\n\t\t}\r\n\t\tc[j] = y;\r\n\t}\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tfor (j = 0; j < m; j++)\r\n\t\t{\r\n\t\t\tif (j == b[i] && i == c[j])\r\n\t\t\t{\r\n\t\t\t\tprintf(\"Array[%d][%d]=%d\", i, j, a[i][j]);\r\n\t\t\t\tf++;\r\n\t\t\t}\t\t\t\t\r\n\t\t}\r\n\t}\r\n\tif (f == 0)\r\n\t\tprintf(\"None\");\r\n}"
  },
  "3858": {
    "sid": 2480153,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fb(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse if(n==2)\r\n\treturn 1;\r\n\telse\r\n\treturn (fb(n-1)+fb(n-2));\r\n}\r\nint main()\r\n{\r\n\tint n,y;\r\n\tscanf(\"%d\",&n);\r\n\ty=fb(n);\r\n\tprintf(\"%d\",y);\r\n}"
  },
  "1936": {
    "sid": 2480151,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a;\r\n\ta=getchar();\r\n\tchar b[1000];\r\n\tgetchar();\r\n\tgets(b);\r\n\tint i;\r\n\tfor(i=0;i<strlen(b);i++)\r\n\t{\r\n\t\tif(b[i]!=a)\r\n\t\tprintf(\"%c\",b[i]);\r\n\t}\r\n}"
  },
  "2770": {
    "sid": 2480150,
    "code": "C++",
    "content": "#include <stdio.h>\n#include <stdio.h>\n\nint f1(int n)\r\n{\r\n\tif(n<=0)\r\n\treturn 0;\r\n\telse\r\n\t{\r\n\t\tif(n%2==1)\r\n\t\treturn 0;\r\n\t\telse\r\n\t\treturn 1;\r\n\t}\r\n}\r\n\nint main()\r\n{\r\n int n,m;\r\n scanf(\"%d\",&n);\r\n\n\n m=f1(n);\nif (m==1)\r\n  printf(\"True\");\r\n else\r\n  printf(\"False\");\r\n return 0;\r\n}\n"
  },
  "2771": {
    "sid": 2480147,
    "code": "C++",
    "content": "#include <stdio.h>\n#include <stdio.h>\n\nint f1(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse\r\n\treturn f1(n-1)+2*n-1;\r\n}\r\n\nint main()\r\n{\r\n int n,sum;\r\n scanf(\"%d\",&n);  \r\n\n\nsum=f1(n);\nprintf(\"%d\",sum);\r\n return 0;\r\n}\n"
  },
  "2777": {
    "sid": 2480146,
    "code": "C++",
    "content": "#include <stdio.h>\n#include <stdio.h>\n\nvoid f1(int a,int b,int c,int *max,int *min)\r\n{\r\n\tint a1;int a2;\r\n\ta1=(a>b)?a:b;\r\n\ta1=(a1>c)?a1:c;\r\n\ta2=(a>b)?b:a;\r\n\ta2=(a2>c)?c:a2;\r\n\t*max=a1;\r\n\t*min=a2;\r\n}\nint main()\r\n{\r\n int a,b,c,max,min;\r\n scanf(\"%d %d %d\",&a,&b,&c);\r\n\n\n  f1(a,b,c,&max,&min);\nprintf(\"%d %d\",max,min);\r\n return 0;\r\n}\n"
  },
  "3814": {
    "sid": 2480145,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include <stdio.h>\r\n\r\nint fac(int a)\r\n{\r\n\tif(a==1)\r\n\treturn 2;\r\n\telse\r\n\treturn fac(a-1)+2*a;\r\n}\r\n\r\nint main(int argc, char *argv[])\r\n\r\n{\r\n\r\n\tint n;\r\n\r\n\tscanf(\"%d\",&n);\r\n\r\n\tprintf(\"%d\",fac(n));\r\n\r\n\treturn 0;\r\n\r\n}"
  },
  "3880": {
    "sid": 2480144,
    "code": "C",
    "content": "#include <stdio.h>\n#include <stdio.h>\n#include<stdio.h> \r\nint add(int x)\r\n{\r\n\tif(x==1)\r\n\treturn 1;\r\n\telse if(x==2)\r\n\treturn 1;\r\n\telse\r\n\treturn (add(x-1)+add(x-2));\r\n} \r\nint main(int argc, char *argv[])\r\n { \r\n int n; \r\n scanf(\"%d\",&n);\r\n  printf(\"%d\",add(n));\r\n  return 0; \r\n} "
  },
  "4224": {
    "sid": 2480142,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tint a,b,c;\r\n\tint sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d%d%d\",&a,&b,&c);\r\n\t\tif((a==1&&b==1&&c==0)||(a==1&&b==0&&c==1)||(a==0&&b==1&&c==1)||(a==1&&b==1&&c==1))\r\n\t\tsum++;\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "4221": {
    "sid": 2480141,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[7]={'1','4','3','3','2','2','3'};\r\n\tchar b[7]={'1','3','4','3'};\r\n\tchar c[7]={'1','4','3','3','2','2','3'};\r\n\tint i;\r\n\tif(strcmp(a,b)==0)\r\n\t{\r\n\t\tfor(i=0;i<strlen(a);i++)\r\n\t\t{\r\n\t\t\tif(i==0)\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\" \");\r\n\t\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\telse\r\n\t{\r\n\t\tif(strcmp(a,c)==0)\r\n\t\t{\r\n\t\t\t\r\n\t\tfor(i=0;i<strlen(a);i++)\r\n\t\t{\r\n\t\t\tif(i==0)\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\" \");\r\n\t\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\t}\r\n\t\t}\r\n\t\t}\r\n\t\telse if(strcmp(b,c)==0)\r\n\t\t{\r\n\t\t\tfor(i=0;i<strlen(b);i++)\r\n\t\t{\r\n\t\t\tif(i==0)\r\n\t\t\tprintf(\"%c\",b[i]);\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\" \");\r\n\t\t\t\tprintf(\"%c\",b[i]);\r\n\t\t\t}\r\n\t\t}\r\n\t\t}\r\n\t}\r\n\t\r\n    \r\n} "
  },
  "4236": {
    "sid": 2480140,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[10];\r\n\tint i;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint min;\r\n\tmin=9;\r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<9;i++)\r\n\t{\r\n\t\tfor(j=0;j<9-i;j++)\r\n\t\t{\r\n\t\t\tif(a[j]>a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tint x;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(a[i]!=0)\r\n\t\t{\r\n\t\t\tif(a[i]<min)\r\n\t\t\t{\r\n\t\t\t\tmin=a[i];\r\n\t\t\t\tx=i;\r\n\t\t\t}\r\n\t\t} \r\n\t}\r\n  \tprintf(\"%d\",min);\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==x)\r\n\t\tcontinue;\r\n\t\telse\r\n\t\tprintf(\"%d\",a[i]);\r\n\t}\r\n}"
  },
  "4203": {
    "sid": 2480139,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tint a[1000];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint j;\r\n\tint x;\r\n\tint y;\r\n\tint t;\r\n\tint sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tx=0;\r\n\t\ty=0;\r\n\t\tfor(j=0;j<n-i;j++)\r\n\t\t{\r\n\t\t\tif(x<a[j])\r\n\t\t\t{\r\n\t\t\t\tx=a[j];\r\n\t\t\t\ty=j;\r\n\t\t\t}\r\n\t\t} \r\n\t\tif(y==n-i-1)\r\n\t\tcontinue;\r\n\t\telse\r\n\t\t{\r\n\t\t\tt=a[y];\r\n\t\t\ta[y]=a[n-i-1];\r\n\t\t\ta[n-i-1]=t;\r\n\t\t\tsum++;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "4206": {
    "sid": 2480138,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tint a[10000];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t} \r\n\tfloat sum=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]==0)\r\n\t\tsum+=2;\r\n\t\telse\r\n\t    sum=sum+(1.0/a[i]);\r\n\t}\r\n\tprintf(\"%.4f\",sum);\r\n}"
  },
  "2604": {
    "sid": 2480137,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nstruct Node{\r\n\tint data;\r\n\tstruct Node *next;\r\n};\r\nstruct Node *createList()\r\n{\r\n\tstruct Node *headNode=(struct Node*)malloc(sizeof(struct Node));\r\n\theadNode->data=1;\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nstruct Node *createNode(int data)\r\n{\r\n\tstruct Node *newNode=(struct Node*)malloc(sizeof(struct Node));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid printList(struct Node *headNode,int n)\r\n{\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove)\r\n\t{\r\n\t\tif(pMove->data<n)\r\n\t\t{\r\n\t\t\tprintf(\"%d \",pMove->data);\r\n\t\t}\r\n\t\tpMove=pMove->next;\r\n\t}\r\n\tprintf(\"\\n\");\r\n}\r\nvoid insertNodeByHead(struct Node *headNode,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tnewNode->next=headNode->next;\r\n\theadNode->next=newNode;\r\n}\r\nvoid deleteNodeByAppoin(struct Node *headNode,int posData)\r\n{\t\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\r\n\tprintf(\"NULL\");\r\n\telse\r\n\twhile(posNode->data!=posData)\r\n\t{\r\n\t\tposNodeFront=posNode;\r\n\t\tposNode=posNodeFront->next;\r\n\t}\r\n\tposNodeFront->next=posNode->next;\r\n\tfree(posNode);\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[100];\r\n\tint n;\r\n\tstruct Node *list=createList();\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-i-1;j++)\r\n\t\t{\r\n\t\t\tif(a[j]>a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tint sum=0;\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]>m)\r\n\t\t{\r\n\t\t\tfor(j=0;j<i;j++)\r\n\t\t\t{\r\n\t\t\t\tif(a[i]==a[j])\r\n\t\t\t\tbreak;\r\n\t\t\t}\r\n\t\t\tif(j==i)\r\n\t\t\t{\r\n\t\t\t\tsum++;\r\n\t\t\t} \r\n\t\t}\r\n\t\t\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tinsertNodeByHead(list,a[i]);\r\n\t}\r\n\tprintf(\"%d\\n\",sum);\r\n\tprintList(list,m);\r\n\t\r\n}"
  },
  "1804": {
    "sid": 2480135,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[20001], n, i, j, k, f[20001] = { 0 }, m[20001] = { 0 }, s;\r\n\twhile (scanf(\"%d\", &n) != EOF)\r\n\t{\r\n\t\tif (n == 0)\r\n\t\t\tbreak;\r\n\t\ts = 0;\r\n\t\tj = 0;\r\n\t\tk = 2 * n - 1;\r\n\t\tfor (i = 0; i < 2 * n; i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\", &a[i]);\r\n\t\t\tif (i == 0)\r\n\t\t\t\tf[i] = a[i];\r\n\t\t\telse\r\n\t\t\t\tf[i] = f[i - 1] + a[i];\r\n\t\t}\r\n\t\tfor (i=0; i<2*n; i++)\r\n\t\t{\r\n\t\t\t\r\n\t\t\t\tm[i] = f[2*n-1]-(i==0?0:f[i-1]);\r\n\t\t\t\r\n\t\t}\r\n\t\tk = 2 * n - 1;\r\n\t\twhile (j <= 2 * n - 1 && k >= 0)\r\n\t\t{\r\n\t\t\tif (f[j] == m[k])\r\n\t\t\t{\r\n\t\t\t\ts++;\r\n\t\t\t\tj++;\r\n\t\t\t\tk--;\r\n\t\t\t}\r\n\t\t\tif (f[j] > m[k])\r\n\t\t\t{\r\n\t\t\t\tk--;\r\n\t\t\t}\r\n\t\t\tif (f[j] < m[k])\r\n\t\t\t{\r\n\t\t\t\tj++;\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"%d\\n\", s);\r\n\t}\r\n}"
  },
  "1807": {
    "sid": 2480134,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tif(n==1)\r\n\t{\r\n\t\treturn 1;\r\n\t}\r\n\telse\r\n\treturn (fac(n-1)+1)*2;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t\tif(n==0)\r\n\t\tbreak;\r\n\t\tprintf(\"%d\\n\",fac(n));\r\n\t}\r\n} "
  },
  "1808": {
    "sid": 2480133,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tlong long int n;\r\n    long long int a[100];\r\n    long long int i;\r\n\twhile(scanf(\"%lld\",&n)!=EOF)\r\n\t{\r\n\t\tif(n==0)\r\n\t\tbreak;\r\n\t\ta[1]=1;\r\n\t\ta[2]=2;\r\n\t\tfor(i=3;i<=n;i++)\r\n\t\t{\r\n\t\t\ta[i]=a[i-1]+a[i-2];\r\n\t\t}\r\n\t\tprintf(\"%lld\\n\",a[n]);\r\n\t\t\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1811": {
    "sid": 2480132,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tint sum=0;\r\n\tint i;\r\n\tfor(i=1;i<=(n+1)/2;i++)\r\n\t{\r\n\t\tif(n%i==0)\r\n\t\tsum=sum+i;\r\n\t}\r\n\treturn sum;\r\n}\r\nint main()\r\n{\r\n\tint m;\r\n\tint i;\r\n\tscanf(\"%d\",&m);\r\n\tint a,b;\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tscanf(\"%d%d\",&a,&b);\r\n\t\tif(fac(a)==b&&fac(b)==a)\r\n\t\t{\r\n\t\t\tprintf(\"YES\\n\");\r\n\t\t}\r\n\t\telse\r\n\t\tprintf(\"NO\\n\");\r\n\t}\r\n}"
  },
  "1812": {
    "sid": 2480131,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t\tif(n>=0&&n<=100)\r\n\t\t{\r\n\t\t\tif(n>=90)\r\n\t\t\tprintf(\"A\\n\");\r\n\t\t\telse if(n>=80)\r\n\t\t\tprintf(\"B\\n\");\r\n\t\t\telse if(n>=70)\r\n\t\t\tprintf(\"C\\n\");\r\n\t\t\telse if(n>=60)\r\n\t\t\tprintf(\"D\\n\");\r\n\t\t\telse\r\n\t\t\tprintf(\"E\\n\");\t\t\r\n\t\t}\r\n\t\telse\r\n\t\tprintf(\"Score is error!\\n\");\r\n\t}\r\n} "
  },
  "3846": {
    "sid": 2480130,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid fac(int *p)\r\n{\r\n\tint n;\r\n\tn=*p;\r\n\tint i;\r\n\tint sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+i*i;\r\n\t\tprintf(\"sum=%d\\n\",sum);\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tfac(&n);\r\n} "
  },
  "3842": {
    "sid": 2480129,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid max(int *p,int *q)\r\n{\r\n\t*p++;\r\n\t*q=*q-1;\r\n}\r\nint main() \r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tint *p,*q;\r\n\tp=&a;\r\n\tq=&b;\r\n\tmax(p,q);\r\n\tprintf(\"%d %d\",*p,*q);\r\n\r\n}"
  },
  "3843": {
    "sid": 2480128,
    "code": "C",
    "content": "#include<stdio.h>\r\nint *sum(int *p,int *q)\r\n{\r\n\tint i,j;\r\n\tint a,b;\r\n\ta=*p;\r\n\tb=*q;\r\n\tj=a-b;\r\n\tif(j>=0)\r\n\tj=j;\r\n\telse\r\n\tj=-j;\r\n\ti=a*a+b*b; \r\n\t*p=i;\r\n\t*q=j;\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tsum(&a,&b);\r\n\tprintf(\"%d %d\",a,b);\r\n}"
  },
  "3849": {
    "sid": 2480127,
    "code": "C",
    "content": "#include<stdio.h>\r\nvoid sum(int *p,int *q)\r\n{\r\n\tint a,b,m,n;\r\n\ta=*p;\r\n\tb=*q;\r\n\tm=a>b?a:b;\r\n\tif(m==a)\r\n\t{\r\n\t\ta=a/2;\r\n\t\tb=b+a;\r\n\t\tb=b/2;\r\n\t\ta=a+b;\r\n\t}\r\n\telse\r\n\t{\r\n\t\tb=b/2;\r\n\t\ta=a+b;\r\n\t\ta=a/2;\r\n\t\tb=b+a;\r\n\t}\r\n\t*p=a;\r\n\t*q=b;\r\n}\r\nint main()\r\n{\r\n\tint a,b;\r\n\tscanf(\"%d%d\",&a,&b);\r\n\tsum(&a,&b);\r\n\tprintf(\"%d %d\",a,b);\r\n}"
  },
  "1001": {
    "sid": 2480125,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\nchar s[1001] ;\r\nint x ,i ;\r\ni = 0 ;\r\nwhile( scanf(\"%d\",&x )!=EOF )\r\n{\r\ns[i++] = x ;\r\n}\r\ns[i] = '\\0' ;\r\nprintf(\"%s\",s ) ;\r\nreturn 0 ;\r\n}"
  },
  "1937": {
    "sid": 2480124,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfloat x,y;\r\n\tfloat z,a;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%f\",&x);\r\n\t\tif(x<-2)\r\n\t\ty=x*x-sin(x);\r\n\t\telse if(x>=-2&&x<=2)\r\n\t\ty=pow(2,x)+x;\t\t\r\n\t\telse \r\n\t\ty=sqrt(x*x+x+1);\r\n\t\tprintf(\"%.2f\\n\",y);\r\n\t}\r\n}"
  },
  "1938": {
    "sid": 2480123,
    "code": "C",
    "content": "#include<stdio.h>\r\nfloat *fac(float a[],int n)\r\n{\r\n\tint i;\r\n\tfloat t[2];\r\n\tt[0]=a[0];\r\n\tt[1]=a[0];\r\n\tfloat *p;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(t[0]<a[i])\r\n\t\tt[0]=a[i];\r\n\t\tif(t[1]>a[i])\r\n\t\tt[1]=a[i];\r\n\t}\r\n\tp=t;\r\n\treturn p;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i,j;\r\n\tfloat a[1000];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%f\",&a[i]);\r\n\t}\r\n\tfloat *p;\r\n\tp=fac(a,n);\r\n\tprintf(\"%.2f %.2f\",*p,*(p+1));\r\n}"
  },
  "1939": {
    "sid": 2480122,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar x[1000];\r\n\tgets(x);\r\n\tint i;\r\n\tint a=0,b=0,c=0,d=0;\r\n\tfor(i=0;i<strlen(x);i++)\r\n\t{\r\n\t\tif(x[i]>='a'&&x[i]<='z'||x[i]>='A'&&x[i]<='Z')\r\n\t\ta++;\r\n\t\telse if(x[i]==' ')\r\n\t\tb++;\r\n\t\telse if(x[i]>='0'&&x[i]<='9')\r\n\t\tc++;\r\n\t\telse\r\n\t\td++;\r\n\t}\r\n\tprintf(\"%d %d %d %d\",a,c,b,d);\r\n}"
  },
  "1940": {
    "sid": 2480121,
    "code": "C",
    "content": "#include<stdio.h>\r\nfloat fac(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse \r\n\treturn fac(n-1)*n;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfloat sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+(1.0/fac(i));\r\n\t} \r\n\tprintf(\"%.4f\",sum);\r\n}"
  },
  "1941": {
    "sid": 2480120,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[10];\r\n\tint sum=0;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t\tsum=sum+a[i];\r\n\t}\r\n\tsum=sum/10;\r\n\tint s=0;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(a[i]>sum)\r\n\t\ts++;\r\n\t}\r\n\tprintf(\"%d\",s);\r\n}"
  },
  "1943": {
    "sid": 2480119,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\n#include<stdlib.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint a[10];\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint t=abs(a[0]);\r\n\tint j=0;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(t>abs(a[i]))\r\n\t\t{\r\n\t\t\tt=abs(a[i]);\r\n\t\t\tj=i;\r\n\t\t}\r\n\t}\r\n\tint tem;\r\n\ttem=a[j];\r\n\ta[j]=a[9];\r\n\ta[9]=tem;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",a[i]);\r\n\t}\r\n}"
  },
  "1944": {
    "sid": 2480118,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\ndouble fac(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse\r\n\treturn fac(n-1)*n;\r\n}\r\ndouble mypow(double x,int n)\r\n{\r\n\tint i;\r\n\tdouble sum=1;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum*x;\r\n\t}\r\n\treturn sum;\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tdouble x;\r\n\tint n;\r\n\tscanf(\"%lf%d\",&x,&n);\r\n\tdouble sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+(pow(-1,i-1)*mypow(x,i)/fac(i));\r\n\t}\r\n\tprintf(\"%.4lf\",sum);\r\n}"
  },
  "1945": {
    "sid": 2480117,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tdouble x;\r\n\tscanf(\"%lf\",&x);\r\n\tdouble y;\r\n\tif(x<0)\r\n\ty=fabs(x);\r\n\telse if(x<2)\r\n\ty=sqrt(x+1);\r\n\telse if(x<4)\r\n\ty=pow(x+2,5);\r\n\telse\r\n\ty=2*x+5;\r\n\tprintf(\"%.2lf\",y);\r\n}"
  },
  "1946": {
    "sid": 2480116,
    "code": "C",
    "content": "#include<stdio.h>\r\nint ctof(int n)\r\n{\r\n\tdouble f;\r\n\tf=32+n*(9.0/5.0);\r\n\treturn f; \r\n} \r\nint main()\r\n{\r\n\tint i;\r\n\tfor(i=-100;i<=150;i+=5)\r\n\t{\r\n\t\tprintf(\"c=%d->f=%d\\n\",i,ctof(i));\r\n\t}\r\n}"
  },
  "1947": {
    "sid": 2480115,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[100][100];\r\n\tint i,j;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t}\r\n\t}\r\n\tint x,y,z;\r\n\tz=a[0][0];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tif(z<a[i][j])\r\n\t\t\t{\r\n\t\t\t\tz=a[i][j];\r\n\t\t\t\tx=i;\r\n\t\t\t\ty=j;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d %d %d\",z,x+1,y+1);\r\n}"
  },
  "1948": {
    "sid": 2480114,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint x;\r\n\tint a=0,b=0,c=0;\r\n\twhile(scanf(\"%d\",&x)!=EOF)\r\n\t{\r\n\t\tif(x<=0)\r\n\t\tbreak;\r\n\t\tif(x>=85)\r\n\t\ta++;\r\n\t\telse if(x>=60)\r\n\t\tb++;\r\n\t\telse \r\n\t\tc++;\r\n\t}\r\n\tprintf(\">=85:%d\\n\",a);\r\n\tprintf(\"60-84:%d\\n\",b);\r\n\tprintf(\"<60:%d\",c);\r\n} "
  },
  "1949": {
    "sid": 2480113,
    "code": "C",
    "content": "#include<stdio.h>\r\ndouble fac(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 1;\r\n\telse\r\n\treturn fac(n-1)*n;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tdouble sum=0;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tsum=sum+(1.0/fac(i));\r\n\t} \r\n\tprintf(\"sum=%.5lf\",sum);\r\n}"
  },
  "1918": {
    "sid": 2480111,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[10],c[100];\r\n\tint i;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tc[i]=i+1;\r\n\t}\r\n\tint t1;\r\n\tfor(i=0;i<9;i++)\r\n\t{\r\n\t\tfor(j=0;j<9-i;j++)\r\n\t\t{\r\n\t\t\tif(a[j]>a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t\tt1=c[j];\r\n\t\t\t\tc[j]=c[j+1];\r\n\t\t\t\tc[j+1]=t1;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",a[i]);\r\n\t}\r\n\tprintf(\"\\n\");\r\n\tfor(i=0;i<10;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",c[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",c[i]);\r\n\t}\r\n}"
  },
  "1921": {
    "sid": 2480110,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nfloat fac(float x, float n)\r\n{\r\n\tif (n == 1)\r\n\t\treturn sqrt(1 + x);\r\n\telse\r\n\t\treturn sqrt(fac(x,n - 1) + n);\r\n}\r\nint main()\r\n{\r\n\tfloat x, n;\r\n\tscanf(\"%f%f\", &x, &n);\r\n\tprintf(\"%.2f\", fac(x, n));\r\n}"
  },
  "4211": {
    "sid": 2480109,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint m;\r\n\tm=n/2;\r\n\tif(n%2==1)\r\n\tm++;\r\n\tprintf(\"%d\",m);\r\n}"
  },
  "2010": {
    "sid": 2480108,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nstruct Node{\r\n\tint data;\r\n\tstruct Node *next;\r\n};\r\nstruct Node *createList()\r\n{\r\n\tstruct Node *headNode=(struct Node*)malloc(sizeof(struct Node));\r\n\theadNode->data=1;\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nstruct Node *createNode(int data)\r\n{\r\n\tstruct Node *newNode=(struct Node*)malloc(sizeof(struct Node));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid printList(struct Node *headNode)\r\n{\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove)\r\n\t{\r\n\t\tprintf(\"%d \",pMove->data);\r\n\t\tpMove=pMove->next;\r\n\t}\r\n\tprintf(\"\\n\");\r\n}\r\nvoid insertNodeByHead(struct Node *headNode,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tnewNode->next=headNode->next;\r\n\theadNode->next=newNode;\r\n}\r\nvoid weicha(struct Node *headNode,int data,int postion)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode;\r\n\twhile(--postion)\r\n\t{\r\n\t\tposNode=posNode->next;\r\n\t}\r\n\tposNode->next=newNode;\r\n} \r\nvoid deleteNodeByAppoin(struct Node *headNode,int n)\r\n{\t\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\r\n\tprintf(\"NULL\");\r\n\telse\r\n\twhile(--n)\r\n\t{\r\n\t\tposNodeFront=posNode;\r\n\t\tposNode=posNodeFront->next;\r\n\t}\r\n\tposNodeFront->next=posNode->next;\r\n\tfree(posNode);\r\n}\r\nvoid dingdiancharu(struct Node *headNode,int postion,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\t\r\n\tprintf(\"NULL\");\r\n\telse\r\n\t{\r\n\t\twhile(postion--)\r\n\t\t{\r\n\t\t\tposNodeFront=posNode;\r\n\t\t\tposNode=posNodeFront->next;\r\n\t\t}\r\n\t\tnewNode->next=posNode;\r\n\t\tposNodeFront->next=newNode;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint i,n;\r\n\tscanf(\"%d\",&n);\r\n\tstruct Node *list=createList();\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tweicha(list,i,i);\r\n\t}\r\n\tchar c;\r\n\tint x,y;\r\n\tint z;\r\n\twhile(scanf(\"%c\",&c)!=EOF)\r\n\t{\r\n\t\tif(c=='I')\r\n\t\t{\r\n\t\t\tscanf(\"%d%d\",&x,&y);\r\n\t\t\tdingdiancharu(list,x,y);\r\n\t\t}\r\n\t\tif(c=='D')\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&z);\r\n\t\t\tdeleteNodeByAppoin(list,z);\r\n\t\t}\r\n\t\tif(c=='Q')\r\n\t\tbreak;\r\n\t}\r\n\tprintList(list);\r\n}"
  },
  "2034": {
    "sid": 2480107,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nstruct Node{\r\n\tint data;\r\n\tstruct Node *next;\r\n};\r\nstruct Node *createList()\r\n{\r\n\tstruct Node *headNode=(struct Node*)malloc(sizeof(struct Node));\r\n\theadNode->data=1;\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nstruct Node *createNode(int data)\r\n{\r\n\tstruct Node *newNode=(struct Node*)malloc(sizeof(struct Node));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid printList(struct Node *headNode)\r\n{\r\n\tint i=0;\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nvoid insertNodeByHead(struct Node *headNode,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tnewNode->next=headNode->next;\r\n\theadNode->next=newNode;\r\n}\r\nvoid weicha(struct Node *headNode,int data,int postion)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode;\r\n\twhile(--postion)\r\n\t{\r\n\t\tposNode=posNode->next;\r\n\t}\r\n\tposNode->next=newNode;\r\n} \r\nvoid deleteNodeByAppoin(struct Node *headNode,int n)\r\n{\t\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\r\n\tprintf(\"NULL\");\r\n\telse\r\n\twhile(--n)\r\n\t{\r\n\t\tposNodeFront=posNode;\r\n\t\tposNode=posNodeFront->next;\r\n\t}\r\n\tposNodeFront->next=posNode->next;\r\n\tfree(posNode);\r\n}\r\nvoid dingdiancharu(struct Node *headNode,int postion,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\t\r\n\tprintf(\"NULL\");\r\n\telse\r\n\t{\r\n\t\twhile(postion--)\r\n\t\t{\r\n\t\t\tposNodeFront=posNode;\r\n\t\t\tposNode=posNodeFront->next;\r\n\t\t}\r\n\t\tnewNode->next=posNode;\r\n\t\tposNodeFront->next=newNode;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tstruct Node *list=createList();\r\n\tint x;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&x);\r\n\t\tinsertNodeByHead(list,x);\r\n\t}\r\n\tprintList(list);\r\n}"
  },
  "2033": {
    "sid": 2480106,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nstruct Node{\r\n\tint data;\r\n\tstruct Node *next;\r\n};\r\nstruct Node *createList()\r\n{\r\n\tstruct Node *headNode=(struct Node*)malloc(sizeof(struct Node));\r\n\theadNode->data=1;\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nstruct Node *createNode(int data)\r\n{\r\n\tstruct Node *newNode=(struct Node*)malloc(sizeof(struct Node));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid printList(struct Node *headNode)\r\n{\r\n\tint i=0;\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nvoid insertNodeByHead(struct Node *headNode,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tnewNode->next=headNode->next;\r\n\theadNode->next=newNode;\r\n}\r\nvoid weicha(struct Node *headNode,int data,int postion)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode;\r\n\twhile(--postion)\r\n\t{\r\n\t\tposNode=posNode->next;\r\n\t}\r\n\tposNode->next=newNode;\r\n} \r\nvoid deleteNodeByAppoin(struct Node *headNode,int n)\r\n{\t\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\r\n\tprintf(\"NULL\");\r\n\telse\r\n\twhile(--n)\r\n\t{\r\n\t\tposNodeFront=posNode;\r\n\t\tposNode=posNodeFront->next;\r\n\t}\r\n\tposNodeFront->next=posNode->next;\r\n\tfree(posNode);\r\n}\r\nvoid dingdiancharu(struct Node *headNode,int postion,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\t\r\n\tprintf(\"NULL\");\r\n\telse\r\n\t{\r\n\t\twhile(postion--)\r\n\t\t{\r\n\t\t\tposNodeFront=posNode;\r\n\t\t\tposNode=posNodeFront->next;\r\n\t\t}\r\n\t\tnewNode->next=posNode;\r\n\t\tposNodeFront->next=newNode;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tstruct Node *list=createList();\r\n\tint x;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&x);\r\n\t\tinsertNodeByHead(list,x);\r\n\t}\r\n\tprintList(list);\r\n}"
  },
  "2610": {
    "sid": 2480105,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nstruct Node{\r\n\tint data;\r\n\tstruct Node *next;\r\n};\r\nstruct Node *createList()\r\n{\r\n\tstruct Node *headNode=(struct Node*)malloc(sizeof(struct Node));\r\n\theadNode->data=1;\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nstruct Node *createNode(int data)\r\n{\r\n\tstruct Node *newNode=(struct Node*)malloc(sizeof(struct Node));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid printList(struct Node *headNode)\r\n{\r\n\tint i=0;\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nvoid insertNodeByHead(struct Node *headNode,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tnewNode->next=headNode->next;\r\n\theadNode->next=newNode;\r\n}\r\nvoid weicha(struct Node *headNode,int data,int postion)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode;\r\n\twhile(--postion)\r\n\t{\r\n\t\tposNode=posNode->next;\r\n\t}\r\n\tposNode->next=newNode;\r\n} \r\nvoid deleteNodeByAppoin(struct Node *headNode,int n)\r\n{\t\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\r\n\tprintf(\"NULL\");\r\n\telse\r\n\twhile(--n)\r\n\t{\r\n\t\tposNodeFront=posNode;\r\n\t\tposNode=posNodeFront->next;\r\n\t}\r\n\tposNodeFront->next=posNode->next;\r\n\tfree(posNode);\r\n}\r\nvoid dingdiancharu(struct Node *headNode,int postion,int data)\r\n{\r\n\tstruct Node *newNode=createNode(data);\r\n\tstruct Node *posNode=headNode->next;\r\n\tstruct Node *posNodeFront=headNode;\r\n\tif(posNode==NULL)\t\r\n\tprintf(\"NULL\");\r\n\telse\r\n\t{\r\n\t\twhile(postion--)\r\n\t\t{\r\n\t\t\tposNodeFront=posNode;\r\n\t\t\tposNode=posNodeFront->next;\r\n\t\t}\r\n\t\tnewNode->next=posNode;\r\n\t\tposNodeFront->next=newNode;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tint a[1000];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t} \r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-i-1;j++)\r\n\t\t{\r\n\t\t\tif(a[j]<a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\t\r\n\t\t}\r\n\t}\r\n\tstruct Node *list=createList();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tinsertNodeByHead(list,a[i]);\r\n\t}\r\n\tprintList(list);\r\n}"
  },
  "3100": {
    "sid": 2480104,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[100];\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint j=0;\r\n\tfor(i=i-1;i>=0;i--)\r\n\t{\r\n\t\tif(j==0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",a[i]);\r\n\t\tj++;\r\n\t}\r\n} "
  },
  "3102": {
    "sid": 2480102,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <malloc.h>\r\nint main(){\r\nint n;\r\nint i;\r\nfloat *t,*s,*v;\r\nscanf(\"%d\",&n);\r\nt=(float*)malloc(sizeof(float)*n);\r\ns=(float*)malloc(sizeof(float)*n);\r\nv=(float*)malloc(sizeof(float)*n);\r\nfor (int i=0;i<n;i++)\r\n{\r\nscanf(\"%f %f\",&s[i],&t[i]);\r\nv[i]=s[i]/t[i];\r\n}\r\nfor (i=0;i<n;i++)\r\nfor (int j=0;j<n-i-1;j++)\r\n{\r\nif (v[j]<v[j+1])\r\n{\r\nfloat temp=v[j];\r\nv[j]=v[j+1];\r\nv[j+1]=temp;\r\n}\r\n}\r\nfor (i=0;i<n;i++)\r\nprintf(\"%.1f\\n\",v[i]);\r\n}"
  },
  "3103": {
    "sid": 2480101,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a,b,c;\r\n\ta=n%10;\r\n\tb=n%100-a;\r\n\tc=n/100;\r\n\tint sum;\r\n\tsum=a*100+b+c;\r\n\tprintf(\"%d\",sum);\r\n} "
  },
  "3104": {
    "sid": 2480100,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint j;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[100][100];\r\n\tfor(j=0;j<n;j++)\r\n\t{\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tprintf(\"%5d\",a[i][j]);\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "3193": {
    "sid": 2480099,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tstruct man{\r\n\t\tchar name[30];\r\n\t\tint da;\r\n\t\tint xiao;\r\n\t}s[5];\r\n\tint i=0;\r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t    gets(s[i].name);\r\n\t\tscanf(\"%d%d\",&s[i].da,&s[i].xiao);\r\n\t\tgetchar();\r\n\t}\r\n\tint max=0;\r\n\tint sum=0;\r\n\tint jl=0;\r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\tsum=s[i].da+s[i].xiao*2;\r\n\t\tif(max<sum)\r\n\t\t{\r\n\t\t\tmax=sum;\r\n\t\t\tjl=i;\r\n\t\t}\r\n\t\t\r\n\t}\r\n\tint js=0;\r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\tsum=s[i].da+s[i].xiao*2;\r\n\t\tif(sum==max)\r\n\t\tjs++;\r\n\t}\r\n\tif(js==1)\r\n\tputs(s[jl].name);\r\n\telse\r\n\tprintf(\"OT\");\r\n}"
  },
  "3192": {
    "sid": 2480098,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tdouble a,b;\r\n\tdouble y;\r\n\tdouble x;\r\n\tdouble z;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%lf%lf\",&a,&b);\r\n\t\tif(a==0&&b==0)\r\n\t\t{\r\n\t\t\tprintf(\"(-INF,INF)\\n\");\r\n\t\t}\r\n\t\telse if(a==0&&b>0)\r\n\t\t{\r\n\t\t\ty=0;\r\n\t\t\tprintf(\"[%.2lf,INF)\\n\",y);\r\n\t\t}\r\n\t\telse if(a==0&&b<0)\r\n\t\t{\r\n\t\t\ty=0;\r\n\t\t\tprintf(\"(-INF,%.2f]\\n\",y);\r\n\t\t}\r\n\t\telse if(a>0&&b>=0)\r\n\t\t{\r\n\t\t\ty=0;\r\n\t\t\tprintf(\"[%.2lf,INF)\\n\",y);\r\n\t\t}\r\n\t\telse if(a>0&&b<0)\r\n\t\t{\r\n\t\t\tx=0;\r\n\t\t\ty=sqrt(-b/a);\r\n\t\t\tz=-sqrt(-b/a);\r\n\t\t\tprintf(\"[%.2lf,%.2lf] U [%.2lf,INF)\\n\",z,x,y);\r\n\t\t}\r\n\t\telse if(a<0&&b<=0)\r\n\t\t{\r\n\t\t\tx=0;\r\n\t\t\tprintf(\"(-INF,%.2lf]\\n\",x);\r\n\t\t}\r\n\t\telse if(a<0&&b>0)\r\n\t\t{\r\n\t\t\tx=0;\r\n\t\t\ty=sqrt(b/-a);\r\n\t\t\tz=-sqrt(b/-a);\r\n\t\t\tprintf(\"(-INF,%.2lf] U [%.2lf,%.2lf]\\n\",z,x,y);\r\n\t\t}\r\n\t}\r\n}"
  },
  "2051": {
    "sid": 2480096,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct Node\r\n{\r\n     int data;  \r\n    struct Node *next;\r\n}LNode,*LinkList; \r\nLNode *createList()\r\n{\r\n\tLinkList headNode=(LinkList)malloc(sizeof(LNode));\r\n\theadNode->next=headNode;\r\n\treturn headNode;\r\n}\r\nLNode *createNode(int data)\r\n{\r\n\tLinkList newNode=(LinkList)malloc(sizeof(LNode));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid dingdian(LinkList headNode,int data,int i)\r\n{\r\n\tLNode *newNode=createNode(data);\t\r\n\tLNode *posnode;\r\n\tLNode *posnodefront;\r\n\tposnodefront=headNode;\r\n\tposnode=headNode->next; \r\n\twhile(--i)\r\n\t{\r\n\t\tposnodefront=posnode;\r\n\t\tposnode=posnodefront->next;\t\r\n\t}\r\n\tnewNode->next=posnode;\r\n\tposnodefront->next=newNode;\r\n}\r\nvoid printList(struct Node *headNode)\r\n{\r\n\tint i=0;\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove!=headNode)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint n;\r\n\tint m;\r\n\tLinkList list=createList();\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&m);\r\n\t\tdingdian(list,m,i);\r\n\t}\r\n\tprintList(list); \r\n}"
  },
  "2052": {
    "sid": 2480095,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct Node\r\n{\r\n     int data;  \r\n    struct Node *next;\r\n}LNode,*LinkList; \r\nLNode *createList()\r\n{\r\n\tLinkList headNode=(LinkList)malloc(sizeof(LNode));\r\n\theadNode->next=headNode;\r\n\treturn headNode;\r\n}\r\nLNode *createNode(int data)\r\n{\r\n\tLinkList newNode=(LinkList)malloc(sizeof(LNode));\r\n\tnewNode->data=data;\r\n\tnewNode->next=NULL;\r\n\treturn newNode;\r\n}\r\nvoid dingdian(LinkList headNode,int data,int i)\r\n{\r\n\tLNode *newNode=createNode(data);\t\r\n\tLNode *posnode;\r\n\tLNode *posnodefront;\r\n\tposnodefront=headNode;\r\n\tposnode=headNode->next; \r\n\twhile(--i)\r\n\t{\r\n\t\tposnodefront=posnode;\r\n\t\tposnode=posnodefront->next;\t\r\n\t}\r\n\tnewNode->next=posnode;\r\n\tposnodefront->next=newNode;\r\n}\r\nint tidata(LinkList headNode,int i)\r\n{\r\n\tLinkList pmove=headNode->next;\r\n\twhile(--i)\r\n\t{\r\n\t\tpmove=pmove->next;\r\n\t}\r\n\treturn pmove->data;\r\n} \r\nvoid printList(struct Node *headNode)\r\n{\r\n\tint i=0;\r\n\tstruct Node *pMove=headNode->next;\r\n\twhile(pMove!=headNode)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\tpMove=pMove->next;\r\n\t\ti++;\r\n\t}\r\n}\r\nint paixu(int *p,int n)\r\n{\r\n\tint i;\r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-1-i;j++)\r\n\t\t{\r\n\t\t\tif(*(p+j)>*(p+1+j))\r\n\t\t\t{\r\n\t\t\t\tt=*(p+j);\r\n\t\t\t\t*(p+j)=*(p+j+1);\r\n\t\t\t\t*(p+j+1)=t; \r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}\r\nvoid jiaoji(int *a,int m,int *b,int n,LinkList list)\r\n{\r\n\tint i;\r\n\tint j;\r\n\tint s=1;\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tif(*(a+i)==*(b+j))\r\n\t\t\t{\r\n\t\t\t\tdingdian(list,*(a+i),s);\r\n\t\t\t\ts++;\r\n\t\t\t}\r\n\t\t} \r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint n;\r\n\tint m;\r\n\tint j;\r\n\tLinkList list=createList();\r\n\tint a[100],b[100];\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint t;\r\n\tpaixu(a,n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tdingdian(list,a[i-1],i);\r\n\t}\r\n\tLinkList List=createList();\r\n\tint mn;\r\n\tscanf(\"%d\",&mn);\r\n\tint w;\r\n\tfor(i=0;i<mn;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&b[i]);\r\n\t} \r\n\tpaixu(b,mn);\r\n\tfor(i=1;i<=mn;i++)\r\n\t{\r\n\t\tdingdian(List,b[i-1],i);\r\n\t}\r\n\tint x,y;\r\n\tint js=0;\r\n\tLinkList listc=createList();\r\n\tint c[100];\r\n\tjiaoji(a,n,b,mn,listc);\r\n\tprintList(listc);\r\n}"
  },
  "1544": {
    "sid": 2480094,
    "code": "C",
    "content": "#include <stdio.h>\r\nconst int N=1<<29;\r\nint a[15],min1,max1,b,k;\r\nvoid make()\r\n{\r\n    for(int i=0; i<10; i++)\r\n    {\r\n\r\n        if(a[i]<min1)\r\n        {\r\n            b=i;\r\n            min1=a[i];\r\n        }\r\n    }\r\n    int temp;\r\n    temp=a[b];\r\n    a[b]=a[0];\r\n    a[0]=temp;\r\n    for(int i=0; i<10; i++)\r\n    {\r\n        if(a[i]>max1)\r\n        {\r\n            k=i;\r\n            max1=a[i];\r\n        }\r\n    }\r\n    temp=a[k];\r\n    a[k]=a[9];\r\n    a[9]=temp;\r\n\r\n}\r\nvoid print()\r\n{\r\n    int i;\r\n    for(i=0; i<10; i++)\r\n    {\r\n        printf(\"%d \",a[i]);\r\n    }\r\n}\r\nint main()\r\n{\r\n\r\n    scanf(\"%d\",&a[0]);\r\n    {\r\n        min1=N;\r\n        max1=-N;\r\n        for(int i=1; i<10; i++)\r\n        {\r\n            scanf(\"%d\",&a[i]);\r\n        }\r\n        make();\r\n        print();\r\n    }\r\n}\r\n"
  },
  "1545": {
    "sid": 2480093,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[n];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=n-m;i<n;i++)\r\n\t{\r\n\t\tif(i==n-m)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",a[i]);\r\n\t}\r\n\tfor(i=0;i<n-m;i++)\r\n\t{\r\n\t\tprintf(\" %d\",a[i]);\r\n\t}\r\n}"
  },
  "1546": {
    "sid": 2480092,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint i;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[n];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ta[i]=i+1;\r\n\t}\r\n\tint j=0;\r\n\tint x=0;\r\n\tfor(i=1;i<=(n-1)*3;)\r\n\t{\r\n\t\tif(x%n==0)\r\n\t\tx=0;\r\n\t\tif(a[x]!=0) \r\n\t\t{\r\n\t\t\tj++;\r\n\t\t\ti++;\r\n\t\t}\r\n\t\tif(j%3==0)\r\n\t\t{\r\n\t\t\ta[x]=0;\r\n\t\t}\r\n\t\tx++;\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]!=0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t}\r\n}"
  },
  "3708": {
    "sid": 2480090,
    "code": "C",
    "content": "#include<stdio.h>\r\nstruct man{\r\n\tint hao;\r\n\tchar name[20];\r\n\tchar zhong;\r\n\tunion{\r\n\t\tint ban;\r\n\t\tchar position[20];\r\n\t}x;\r\n}s;\r\nint main()\r\n{\r\n\tscanf(\"%d %s %c\",&s.hao,&s.name,&s.zhong);\r\n\tif(s.zhong=='t')\r\n\t{\r\n\t\tscanf(\"%s\",&s.x.position);\r\n\t\tprintf(\"%d %s %c %s\",s.hao,s.name,s.zhong,s.x.position);\r\n\t}\r\n\tif(s.zhong=='s')\r\n\t{\r\n\t\tscanf(\"%d\",&s.x.ban);\r\n\t\tprintf(\"%d %s %c %d\",s.hao,s.name,s.zhong,s.x.ban);\r\n\t}\r\n\t\r\n}"
  },
  "2053": {
    "sid": 2480087,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct Node\r\n{\r\n    int data;   \r\n   struct Node *next;\r\n}LNode,*LinkList;\r\nLinkList createList()\r\n{\r\n\tLinkList headNode=(LinkList)malloc(sizeof(LNode));\r\n\theadNode->next=headNode;\r\n}\r\nLinkList createNode(int data)\r\n{\r\n\tLinkList posNode=(LinkList)malloc(sizeof(LNode));\r\n\tposNode->data=data;\r\n\tposNode->next=NULL;\r\n}\r\nvoid dingdian(LinkList headNode,int data,int position)\r\n{\r\n\tLinkList newNode=createNode(data);\r\n\tLinkList posnode=headNode->next;\r\n\tLinkList posfront=headNode;\r\n\twhile(--position)\r\n\t{\r\n\t\tposfront=posfront->next;\r\n\t\tposnode=posfront->next;\r\n\t} \r\n\tnewNode->next=posnode;\r\n\tposfront->next=newNode;\r\n}\r\n/*void dingdian(LinkList headNode,int data,int position)\r\n{\r\n\tLinkList newNode=createNode(data);\r\n\tLinkList posnode=headNode->next;\r\n\twhile(--position)\r\n\t{\r\n\t\tposnode=posnode->next;\r\n\t} \r\n\tnewNode->next=posnode->next;\r\n\tposnode->next=newNode;\r\n}*/\r\nvoid printList(LinkList headNode)\r\n{\r\n\tLinkList pMove=headNode->next;\r\n\tint i=0;\r\n\twhile(pMove!=headNode)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",pMove->data);\r\n\t\telse \r\n\t\tprintf(\" %d\",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nvoid paixu(int *p,int n)\r\n{\r\n\tint i;\r\n\tint j;\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-1-i;j++)\r\n\t\t{\r\n\t\t\tif(*(p+j)>*(p+j+1))\r\n\t\t\t{\r\n\t\t\t\tt=*(p+j);\r\n\t\t\t\t*(p+j)=*(p+j+1);\r\n\t\t\t\t*(p+j+1)=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}\r\nint chazhao(LinkList headNode,int x)\r\n{\r\n\tint i=0;\r\n\tLinkList pMove=headNode->next;\r\n\twhile(pMove!=headNode)\r\n\t{\r\n\t\tif(pMove->data==x)\r\n\t\t{\r\n\t\t\ti++;\r\n\t\t}\r\n\t\tpMove=pMove->next;\r\n\t}\r\n\tif(i==0)\r\n\treturn 0;\r\n\telse \r\n\treturn 1;\r\n}\r\nint xiao(int a[],int n,int x)\r\n{\r\n\tint i;\r\n\tint j=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]==x)\r\n\t\tj++;\r\n\t}\r\n\tif(j==0)\r\n\treturn 0;\r\n\telse \r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[100];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tint y;\r\n\ty=xiao(a,n,m);\r\n\tif(y==0)\r\n\t{\r\n\t\tn=n+1;\r\n\t\ta[n-1]=m;\r\n\t}\r\n\tpaixu(a,n);\r\n\tLinkList list=createList();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tdingdian(list,a[i],i+1);\r\n\t}\r\n\tprintf(\"%d\\n\",y);\r\n\tprintList(list);\r\n} "
  },
  "1206": {
    "sid": 2480086,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[100][100];\r\n\tint i;\r\n\tint j;\r\n\tint max=a[0][0];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tif(max<a[i][j])\r\n\t\t\t{\r\n\t\t\t\tmax=a[i][j];\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",max);\r\n}"
  },
  "1214": {
    "sid": 2480084,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,m;\r\n\twhile(scanf(\"%d%d\",&n,&m)!=EOF)\r\n\t{\r\n\t\tif(n==0&&m==0)\r\n\t\t{\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tint sum;\r\n\t\tsum=n;\r\n\t\tint i;\r\n\t\tfor(i=1;i<m;i++)\r\n\t\t{\r\n\t\t\tsum=sum*n;\r\n\t\t\tif(sum>=1000)\r\n\t\t\t{\r\n\t\t\t\tsum=sum%1000;\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"%d\\n\",sum);\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1216": {
    "sid": 2480082,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint w;\r\n\tfor(w=0;w<n;w++)\r\n\t{\r\n\t\tint m;\r\n\t\tscanf(\"%d\",&m);\r\n\t\tif(m<=1)\r\n\t\t{\r\n\t\t\tprintf(\"No\");\r\n\t\t\tcontinue;\r\n\t\t}\r\n\t\tint i;\r\n\t\tint a[1000];\r\n\t\tfor(i=0;i<m;i++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i]);\r\n\t\t}\r\n\t\tint j;\r\n\t\tint max=a[0];\r\n\t\tfor(i=0;i<m;i++)\r\n\t\t{\r\n\t\t\tif(max<a[i])\r\n\t\t\tmax=a[i];\r\n\t\t}\r\n\t\tint sum=0;\r\n\t\tfor(i=0;i<m;i++)\r\n\t\t{\r\n\t\t\tif(a[i]!=max)\r\n\t\t\tsum=sum+a[i]; \r\n\t\t}\r\n\t\tif(max>sum+1)\r\n\t\tprintf(\"No\\n\");\r\n\t\telse\r\n\t\tprintf(\"Yes\\n\");\r\n\t}\r\n}"
  },
  "3707": {
    "sid": 2480079,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tstruct man{\r\n\t\tint hao;\r\n\t\tint nian;\r\n\t\tstruct{\r\n\t\t\tint a;\r\n\t\t\tint b;\r\n\t\t\tint c;\r\n\t\t\tint d;\r\n\t\t}x;\t\r\n\t}s[3];\r\n\tint i;\r\n\tint v;\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tscanf(\"%d%d\",&s[i].hao,&s[i].nian);\r\n\t\tif(s[i].nian==1)\r\n\t\tscanf(\"%d%d%d\",&s[i].x.a,&s[i].x.b,&s[i].x.c);\r\n\t\telse if(s[i].nian==2)\r\n\t\tscanf(\"%d%d\",&s[i].x.a,&s[i].x.b);\r\n\t\telse if(s[i].nian==3)\r\n\t\tscanf(\"%d%d%d%d\",&s[i].x.a,&s[i].x.b,&s[i].x.c,&s[i].x.d);\r\n\t}\r\n\r\n\tfor(i=0;i<3;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\t{\r\n\t\t\tif(s[i].nian==1)\r\n\t\t\tprintf(\"%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b+s[i].x.c);\r\n\t\t\telse if(s[i].nian==2)\r\n\t\t\tprintf(\"%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b);\r\n\t\t\telse if(s[i].nian==3)\r\n\t\t\tprintf(\"%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b+s[i].x.c+s[i].x.d);\r\n\t\t}\r\n\t\telse \r\n\t\t{\r\n\t\t\tif(s[i].nian==1)\r\n\t\t\tprintf(\"\\n%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b+s[i].x.c);\r\n\t\t\telse if(s[i].nian==2)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"\\n%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b);\r\n\t\t\t}\r\n\t\t\telse if(s[i].nian==3)\r\n\t\t\tprintf(\"\\n%d %d %d\",s[i].hao,s[i].nian,s[i].x.a+s[i].x.b+s[i].x.c+s[i].x.d);\r\n\t\t}\r\n\t}\r\n}"
  },
  "2606": {
    "sid": 2480076,
    "code": "C",
    "content": "#define _CRT_SECURE_NO_WARNINGS\r\n#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct Node\r\n{\r\n\tint data;\r\n\tstruct Node* next;\r\n}LNode, * LinkList;\r\nLinkList createList()\r\n{\r\n\tLinkList headNode = (LinkList)malloc(sizeof(LNode));\r\n\theadNode->next = NULL;\r\n\treturn headNode;\r\n}\r\nLinkList createNode(int data)\r\n{\r\n\tLinkList posNode = (LinkList)malloc(sizeof(LNode));\r\n\tposNode->data = data;\r\n\tposNode->next = NULL;\r\n}\r\n/*void dingdian(LinkList headNode,int data,int position)\r\n{\r\n\tLinkList newNode=createNode(data);\r\n\tLinkList posnode=headNode->next;\r\n\tLinkList posfront=headNode;\r\n\twhile(--position)\r\n\t{\r\n\t\tposfront=posfront->next;\r\n\t\tposnode=posfront->next;\r\n\t}\r\n\tnewNode->next=posnode;\r\n\tposfront->next=newNode;\r\n}*/\r\nvoid dingdian(LinkList headNode, int data, int position)\r\n{\r\n\tLinkList newNode = createNode(data);\r\n\tLinkList posnode = headNode;\r\n\twhile (--position)\r\n\t{\r\n\t\tposnode = posnode->next;\r\n\t}\r\n\tnewNode->next = posnode->next;\r\n\tposnode->next = newNode;\r\n}\r\nvoid printList(LinkList headNode)\r\n{\r\n\tLinkList pMove = headNode->next;\r\n\tint i = 0;\r\n\twhile (pMove != NULL)\r\n\t{\r\n\t\tprintf(\"%d \", pMove->data);\r\n\t\ti++;\r\n\t\tpMove = pMove->next;\r\n\t}\r\n}\r\nvoid chaji(LinkList A, LinkList B, LinkList C, int n, int m)\r\n{\r\n\tLinkList amove = A->next;\r\n\tLinkList bmove = B->next;\r\n\tint i;\r\n\tint j;\r\n\tint z = 1;\r\n\tint k;\r\n\tfor (i = 1; i <= n; i++)\r\n\t{\r\n\t\tk = 0;\r\n\t\tfor (j = 1; j <= m; j++)\r\n\t\t{\r\n\t\t\tif (amove->data == bmove->data)\r\n\t\t\t{\r\n\t\t\t\tk++;\r\n\t\t\t}\r\n\t\t\tbmove = bmove->next;\r\n\t\t}\r\n\t\tif (k == 0)\r\n\t\t{\r\n\t\t\tdingdian(C, amove->data, z);\r\n\t\t\tz++;\r\n\t\t}\r\n\t\tbmove = B->next;\r\n\t\tamove = amove->next;\r\n\t}\r\n}\r\nvoid lianjie(LinkList L1, LinkList L2, int m)\r\n{\r\n\tLinkList posnode = L1;\r\n\tLinkList posfront = L2;\r\n\twhile (m--)\r\n\t{\r\n\t\tposnode = posnode->next;\r\n\t}\r\n\tposnode->next = L2->next;\r\n\tposfront->next = NULL;\r\n}\r\nint main()\r\n{\r\n\tLinkList list = createList();\r\n\tint n,m;\r\n\tint a[1000];\r\n\tint i;\r\n\tscanf(\"%d\",&m);\r\n\tint j;\r\n\tint x=0;\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\t\r\n\t}\r\n\tgetchar();\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=m;i<m+n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint t;\r\n\tint b[1000];\r\n\tfor(i=0;i<m+n;i++)\r\n\t{\r\n\t\tfor(j=0;j<i;j++)\r\n\t\t{\r\n\t\t\tif(a[i]==a[j])\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tif(j==i)\r\n\t\t{\r\n\t\t\tb[x]=a[i];\r\n\t\t\tx++;\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<x-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<x-1-i;j++)\r\n\t\t{\r\n\t\t\tif(b[j]>b[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=b[j];\r\n\t\t\t\tb[j]=b[j+1];\r\n\t\t\t\tb[j+1]=t;\t\t\t\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<x;i++)\r\n\t{\r\n\t\tdingdian(list,b[i],i+1);\t\r\n\t}\r\n\tprintList(list);\r\n}\r\n"
  },
  "2701": {
    "sid": 2480075,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tgets(a);\r\n\tchar b[1000];\r\n\tchar c[1000];\r\n\tint i;\r\n\tint j = 0;\r\n\tfor (i = 0; i < strlen(a); i++)\r\n\t{\r\n\t\tif (a[i] >= '0' && a[i] <= '9')\r\n\t\t{\r\n\t\t\t;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tb[j] = a[i];\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tb[j] = '\\0';\r\n\tj = 0;\r\n\tfor (i = 0; i < strlen(a); i++)\r\n\t{\r\n\t\tif (a[i] >= '0' && a[i] < '9')\r\n\t\t{\r\n\t\t\tc[j] = a[i];\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tc[j] = '\\0';\r\n\tfor (i = 0; i < strlen(b) / 2; i++)\r\n\t{\r\n\t\tprintf(\"%c\", b[i]);\r\n\t}\r\n\tfor (j = 0; j < strlen(c); j++)\r\n\t{\r\n\t\tprintf(\"%c\", c[j]);\r\n\t}\r\n\tfor (; i < strlen(b); i++)\r\n\t{\r\n\t\tprintf(\"%c\", b[i]);\r\n\t}\r\n}"
  },
  "1887": {
    "sid": 2480073,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint pan(int n)\r\n{\r\n\tif(n<=1)\r\n\treturn 0;\r\n\tint k=sqrt(n);\r\n\tint i;\r\n\tfor(i=2;i<=k;i++)\r\n\t{\r\n\t\tif(n%i==0)\r\n\t\treturn 0;\r\n\t}\r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint sum=0;\r\n\tfor(i=100;i<=200;i++)\r\n\t{\r\n\t\tif(pan(i)==1)\r\n\t\tsum++;\r\n\t}\r\n\tprintf(\"%d\\n\",sum);\r\n\tfor(i=100;i<=200;i++)\r\n\t{\r\n\t\tif(pan(i)==1)\r\n\t\t{\r\n\t\t\tprintf(\"%d \",i);\r\n\t\t}\r\n\t}\r\n} "
  },
  "1886": {
    "sid": 2480072,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[10];\r\n\tint i=0;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\twhile(n!=0)\r\n\t{\r\n\t\ta[i]=n%10;\r\n\t\ti++;\r\n\t\tn=n/10;\r\n\t}\r\n\tfor(i=i-1;i>=0;i--)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",a[i]);\r\n\t\telse\r\n\t\tprintf(\"%d \",a[i]);\r\n\t\t\r\n\t}\r\n} "
  },
  "1885": {
    "sid": 2480071,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[4];\r\n\tint i;\r\n\tfor(i=0;i<4;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint j,z;\r\n\tint b[3];\r\n\tint q,w,e;\r\n\tfor(i=0;i<=1;i++)\r\n\t{\r\n\t\tfor(j=1;j<=2;j++)\r\n\t\t{\r\n\t\t\tfor(z=2;z<=3;z++)\r\n\t\t\t{\r\n\t\t\t\tif(i!=j&&j!=z&&i!=z)\r\n\t\t\t\t{\r\n\t\t\t\t\tb[0]=a[i];\r\n\t\t\t\t\tb[1]=a[j];\r\n\t\t\t\t\tb[2]=a[z];\r\n\t\t\t\t\tfor(q=0;q<3;q++)\r\n\t\t\t\t\t{\r\n\t\t\t\t\t\tfor(w=0;w<3;w++)\r\n\t\t\t\t\t\t{\r\n\t\t\t\t\t\t\tif(q==w)\r\n\t\t\t\t\t\t\tcontinue;\r\n\t\t\t\t\t\t\te=3-q-w;\r\n\t\t\t\t\t\t\tif(e>=0&&e<3)\r\n\t\t\t\t\t\t\tprintf(\"%d %d %d\\n\",b[q],b[w],b[e]);\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}\t\t\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
  },
  "1824": {
    "sid": 2480070,
    "code": "C",
    "content": "#include<stdio.h>\r\n#define PI 3.1415927\r\nint main()\r\n{\r\n\tdouble n;\r\n\twhile(scanf(\"%lf\",&n)!=EOF)\r\n\t{\r\n\t\tdouble v;\r\n\t\tv=(4.0/3.0)*PI*n*n*n;\r\n\t\tprintf(\"%.3lf\\n\",v);\r\n\t}\r\n}"
  },
  "5315": {
    "sid": 2480069,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tenum month{\r\n\t\ta1=1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12\r\n\t}w;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tw=(enum month)n;\r\n\tif(w<=4&&w>=2)\r\n\tprintf(\"\u6625\");\r\n\telse if(w>=5&&w<=7)\r\n\tprintf(\"\u590f\");\r\n\telse if(w<=10&&w>=8)\r\n\tprintf(\"\u79cb\");\r\n\telse\r\n\tprintf(\"\u51ac\");\r\n}"
  },
  "1838": {
    "sid": 2480068,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h> \r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tint i;\r\n\tchar a[100][100];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tint j;\r\n\tint z;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tint as[5]={\r\n\t\t0\r\n\t};\r\n\t\tfor(j=0;j<strlen(a[i]);j++)\r\n\t\t{\r\n\t\t\tif(a[i][j]=='a')\r\n\t\t\tas[0]++;\r\n\t\t\telse if(a[i][j]=='e')\r\n\t\t\tas[1]++;\r\n\t\t\telse if(a[i][j]=='i')\r\n\t\t\tas[2]++;\r\n\t\t\telse if(a[i][j]=='o')\r\n\t\t\tas[3]++;\r\n\t\t\telse if(a[i][j]=='u')\r\n\t\t\tas[4]++;\r\n\t\t}\r\n\t\tif(i==0)\r\n\t\t{\r\n\t\t\tprintf(\"a:%d\\n\",as[0]);\r\n\t\t\tprintf(\"e:%d\\n\",as[1]);\r\n\t\t\tprintf(\"i:%d\\n\",as[2]);\r\n\t\t\tprintf(\"o:%d\\n\",as[3]);\r\n\t\t\tprintf(\"u:%d\",as[4]);\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tprintf(\"\\n\\na:%d\\n\",as[0]);\r\n\t\t\tprintf(\"e:%d\\n\",as[1]);\r\n\t\t\tprintf(\"i:%d\\n\",as[2]);\r\n\t\t\tprintf(\"o:%d\\n\",as[3]);\r\n\t\t\tprintf(\"u:%d\",as[4]);\r\n\t\t}\r\n\t}\r\n} "
  },
  "1823": {
    "sid": 2480067,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tdouble x1,y1,x2,y2;\r\n\twhile(scanf(\"%lf%lf%lf%lf\",&x1,&y1,&x2,&y2)!=EOF)\r\n\t{\r\n\t\tdouble a;\r\n\t\tdouble b;\r\n\t\ta=x1-x2;\r\n\t\tb=y1-y2;\r\n\t\tif(a<0)\r\n\t\ta=-a;\r\n\t\tif(b<0)\r\n\t\tb=-b;\r\n\t\tprintf(\"%.2lf\\n\",sqrt(a*a+b*b));\t\t\r\n\t}\r\n}"
  },
  "1893": {
    "sid": 2480065,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tgets(a);\r\n\tchar b[1000];\r\n\tint i;\r\n\tint j=0;\r\n\tfor(i=0;i<strlen(a)-1;i++)\r\n\t{\r\n\t\tif(a[i]>='0'&&a[i]<='9')\r\n\t\t{\r\n\t\t\tb[j]=a[i];\r\n\t\t\tj++;\r\n\t\t}\r\n\t\telse if((a[i]<'0'||a[i]>'9')&&(a[i+1]>='0'&&a[i+1]<='9'))\r\n\t\t{\r\n\t\t\tb[j]='*';\r\n\t\t\tj++;\r\n\t\t}\r\n\t}\r\n\tif(a[strlen(a)-1]>='0'&&a[strlen(a)-1]<='9')\r\n\t{\r\n\t\tb[j]=a[strlen(a)-1];\r\n\t\tb[j+1]='\\0';\r\n\t}\r\n\telse \r\n\t{\r\n\t\tif(a[strlen(a)-2]>='0'&&a[strlen(a)-2]<='9')\r\n\t\t{\r\n\t\t\tb[j]='*';\r\n\t\t\tb[j+1]='\\0';\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tb[j]='\\0';\r\n\t\t}\r\n\t}\r\n\tputs(b);\r\n}"
  },
  "1865": {
    "sid": 2480064,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,n;\r\n\tscanf(\"%d\",&a);\r\n\tscanf(\"%d\",&n);\r\n\tint sum=0;\r\n\tint t=a;\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tsum=sum+a;\r\n\t\ta=a*10+t;\t\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "1821": {
    "sid": 2480063,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint main()\r\n{\r\n\tlong long int n;\r\n\tlong long int m;\r\n\tlong long int n1;\r\n\twhile(scanf(\"%lld\",&n)&&n)\r\n\t{\r\n\t\tn1=pow(5,n)-4;\r\n\t\tint i;\r\n\t\tm=n1;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tm=(m-1)/5*4;\r\n\t\t} \r\n\t\tm=m+n;\r\n\t\tprintf(\"%lld %lld\\n\",n1,m);\r\n\t} \r\n} "
  },
  "1836": {
    "sid": 2480062,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[50][1000];\r\n\tint i;\r\n\tint j=0;\r\n\twhile(1)\r\n\t{\r\n\t\tgets(a[j]);\r\n\t\tint max=(int)a[j][0];\r\n\t\tfor(i=0;i<strlen(a[j]);i++)\r\n\t\t{\r\n\t\t\tif(max<(int)a[j][i])\r\n\t\t\t{\r\n\t\t\t\tmax=(int)a[j][i];\r\n\t\t\t}\r\n\t\t}\r\n\t\tfor(i=0;i<strlen(a[j]);i++)\r\n\t\t{\r\n\t\t\tif((int)a[j][i]==max)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%c\",a[j][i]);\r\n\t\t\t\tprintf(\"(max)\");\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%c\",a[j][i]);\r\n\t\t\t}\r\n\t\t}\r\n\t\tprintf(\"\\n\");\r\n\t\tj++;\r\n\t\tif(j>=49)\r\n\t\t{\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "2608": {
    "sid": 2480061,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\n#include<string.h>\r\ntypedef struct Node\r\n{\r\n\tchar data[20];\r\n\tstruct Node* next;\r\n}LNode, * LinkList;\r\nLinkList createList()\r\n{\r\n\tLinkList headNode = (LinkList)malloc(sizeof(LNode));\r\n\theadNode->next = NULL;\r\n\treturn headNode;\r\n}\r\nLinkList createNode(char data[])\r\n{\r\n\tLinkList newNode = (LinkList)malloc(sizeof(LNode));\r\n\tstrcpy(newNode->data, data);\r\n\tnewNode->next = NULL;\r\n\treturn newNode;\r\n}\r\nvoid dingdian(LinkList headNode, char data[], int i)\r\n{\r\n\t/*LinkList newNode = createNode(data);\r\n\tLinkList posNode = headNode->next;\r\n\ti = i + 1;\r\n\twhile (--i)\r\n\t{\r\n\t\tposNode = posNode->next;\r\n\t}\r\n\tnewNode->next = posNode;\r\n\tposNode = newNode;*/\r\n\tLinkList newNode = createNode(data);\r\n\tLinkList posnode = headNode;\r\n\twhile (--i)\r\n\t{\r\n\t\tposnode = posnode->next;\r\n\t}\r\n\tnewNode->next = posnode->next;\r\n\tposnode->next = newNode;\r\n}\r\nint jiancha(LinkList headNode, char data[])\r\n{\r\n\tLinkList pMove = headNode->next;\r\n\twhile (pMove!= NULL)\r\n\t{\r\n\t\tif (strcmp(pMove->data, data) == 0)\r\n\t\t\treturn 0;\r\n\t\tpMove = pMove -> next;\r\n\t}\r\n\treturn 1;\r\n}\r\nvoid printList(LinkList headNode)\r\n{\r\n\tLinkList pMove = headNode->next;\r\n\tint i = 0;\r\n\twhile (pMove != NULL)\r\n\t{\r\n\t\tif (i == 0)\r\n\t\t\tprintf(\"%s\", pMove->data);\r\n\t\telse\r\n\t\t\tprintf(\" %s\", pMove->data);\r\n\t\ti++;\r\n\t\tpMove = pMove->next;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tint i;\r\n\tLinkList list = createList();\r\n\tchar a[20];\r\n\tscanf(\"%d\", &n);\r\n\tint j = 0;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tscanf(\"%s\", &a);\r\n\t\tif (jiancha(list, a) == 1)\r\n\t\t{\r\n\t\t\tdingdian(list, a, j+1);\r\n\t\t\tj++;\r\n\t\t}\r\n\t\t\t\r\n\t}\r\n\tprintList(list);\r\n}\r\n"
  },
  "1818": {
    "sid": 2480060,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\nint main()\r\n{\r\n\tint n,m;\r\n\tint a[10000],b[10000];\r\n\tint i;\r\n\tint j;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&b[i]);\r\n\t}\r\n\tint min=abs(a[0]-b[0]); \r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tif(min>abs(a[i]-b[j]))\r\n\t\t\tmin=abs(a[i]-b[j]);\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",min);\r\n}"
  },
  "4214": {
    "sid": 2480059,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tdouble x[n],y[n];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%lf%lf\",&x[i],&y[i]);\r\n\t}\r\n\tint j;\r\n\tdouble max=(y[1]-y[0])/(x[1]-x[0]);\r\n\tdouble t;\r\n\tfor(i=1;i<n;i++)\r\n\t{\r\n\t\tt=(y[i]-y[i-1])/(x[i]-x[i-1]);\r\n\t\tif(max<t)\r\n\t\t{\r\n\t\t\tmax=t;\r\n\t\t}\t\r\n\t}\r\n\tprintf(\"%.2f\",max);\r\n}\t\t"
  },
  "4222": {
    "sid": 2480058,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tfloat a[10000],b[10000];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%f%f\",&a[i],&b[i]);\r\n\t}\r\n\tfloat k;\r\n\tfloat m;\r\n\tif(a[1]-a[0]==0)\r\n\t{\r\n\t\tfloat q=a[0];\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tif(a[i]==q)\r\n\t\t\tcontinue;\r\n\t\t\telse\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tif(i==n)\r\n\t\tprintf(\"Mai!MaiDaKuaiDe\");\r\n\t\telse\r\n\t\tprintf(\"SuanLeBa\");\r\n\t}\r\n\telse\r\n\t{\r\n\t\tk=(b[1]-b[0])/(a[1]-a[0]);\r\n\t\tm=b[0]-k*a[0];\r\n\t\tfor(i=2;i<n;i++)\r\n\t\t{\r\n\t\t\tif(b[i]==k*a[i]+m)\r\n\t\t\tcontinue;\r\n\t\t\telse\r\n\t\t\tbreak;\r\n\t\t}\r\n\t\tif(i==n)\r\n\t\tprintf(\"Mai!MaiDaKuaiDe\");\r\n\t\telse\r\n\t\tprintf(\"SuanLeBa\");\r\n\t}\r\n\treturn 0;\r\n}\r\n"
  },
  "2654": {
    "sid": 2480057,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[10000];\r\n\tgets(a);\r\n\tint i;\r\n\tint b[127]={\r\n\t\t0\r\n\t};\r\n\tint t;\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tt=a[i];\r\n\t\tb[t]++;\r\n\t}\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tt=a[i];\r\n\t\tif(b[t]==1)\r\n\t\t{\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\tbreak;\r\n\t\t}\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "2675": {
    "sid": 2480056,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tchar b[100];\r\n\tchar c[100];\r\n\tgets(a);\r\n\tgets(b);\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tc[i]=b[i];\r\n\t} \r\n\tint j=i;\r\n\tint z=0;\r\n\tfor(;i<n+strlen(a);i++)\r\n\t{\r\n\t\tc[i]=a[z];\r\n\t\tz++;\r\n\t}\r\n\tint t;\r\n\tfor(;i<strlen(a)+strlen(b);i++)\r\n\t{\r\n\t\tc[i]=b[j];\r\n\t\tj++;\r\n\t}\r\n\tputs(c);\r\n}"
  },
  "2680": {
    "sid": 2480055,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tint i;\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tif((a[i]>='A'&&a[i]<='Z')||(a[i]>='a'&&a[i]<='z')||(a[i]>='0'&&a[i]<='9'))\r\n\t\t{\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tif(i==0)\r\n\t\t\t{\r\n\t\t\t\tcontinue;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tif((a[i-1]>='A'&&a[i-1]<='Z')||(a[i-1]>='a'&&a[i-1]<='z')||(a[i-1]>='0'&&a[i-1]<='9'))\r\n\t\t\t\t{\r\n\t\t\t\t\tprintf(\"\\n\");\r\n\t\t\t\t}\r\n\t\t\t\telse\r\n\t\t\t\t{\r\n\t\t\t\t\tcontinue;\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
  },
  "2683": {
    "sid": 2480054,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tchar t;\r\n\tgets(a);\r\n\tint i,j;\r\n\tfor(i=0;i<strlen(a)-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<strlen(a)-1-i;j++)\r\n\t\t{\r\n\t\t\tif((int)a[j]>(int)a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\t\t\r\n\t\t}\r\n\t}\t\r\n\tputs(a);\r\n}"
  },
  "2685": {
    "sid": 2480053,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tint i;\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tif(n==0)\r\n\t{\r\n\t\tputs(a);\r\n\t}\r\n\telse\r\n\t{\r\n\t\tfor(i=0;i<strlen(a);i++)\r\n\t\t{\r\n\t\t\tprintf(\"%c\",a[i]);\r\n\t\t\tif((i+1)%n==0)\r\n\t\t\tprintf(\"\\n\");\r\n\t\t} \r\n\t}\r\n}"
  },
  "2713": {
    "sid": 2480052,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[100][100];\r\n\tint i,j;\r\n\tint b[100]={\r\n\t\t0\r\n\t};\r\n\tint c[100];\r\n\tint tem;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ttem=0;\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\ttem+=a[i][j];\r\n\t\t}\r\n\t\tb[i]=tem;\r\n\t\tc[i]=i;\r\n\t}\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-1-i;j++)\r\n\t\t{\r\n\t\t\tif(b[j]>b[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=b[j];\r\n\t\t\t\tb[j]=b[j+1];\r\n\t\t\t\tb[j+1]=t;\r\n\t\t\t\tt=c[j];\r\n\t\t\t\tc[j]=c[j+1];\r\n\t\t\t\tc[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tt=c[i];\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tif(j==0)\r\n\t\t\tprintf(\"%d\",a[t][j]);\r\n\t\t\telse\r\n\t\t\tprintf(\" %d\",a[t][j]);\r\n\t\t} \r\n\t\tif(i!=n-1)\r\n\t\tprintf(\"\\n\");\r\n\t} \r\n} "
  },
  "4226": {
    "sid": 2480051,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint t;\r\n\tt=(10-n)*100-10+n;\r\n\tprintf(\"%d\",t);\r\n}"
  },
  "4239": {
    "sid": 2480050,
    "code": "C",
    "content": "#include<stdio.h>\r\nint pan(int a[],int n)\r\n{\r\n\tint i;\r\n\tint s=a[0];\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(a[i]!=s)\r\n\t\treturn 0;\r\n\t}\r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tint a[100];\r\n\tint i;\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\ta[i]=i+1;\r\n\t}\r\n\tint j=0;\r\n\tint b[100];\r\n\twhile(1)\r\n\t{\r\n\t\tb[j]=j%n+1;\r\n\t\ta[j]-=j+1;\r\n\t\tj++;\r\n\t\tif(pan(a,n)==1)\r\n\t\tbreak;\r\n\t}\r\n\tprintf(\"%d\\n\",j);\r\n\tfor(i=0;i<j;i++)\r\n\t{\r\n\t\tif(i==0)\r\n\t\tprintf(\"%d\",b[i]);\r\n\t\telse\r\n\t\tprintf(\" %d\",b[i]);\r\n\t}\r\n}"
  },
  "4240": {
    "sid": 2480049,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint pos(int m,int n)\r\n{\r\n\tif(n==0)\r\n\treturn 1;\r\n\tint i;\r\n\tfor(i=1;i<n;i++)\r\n\t{\r\n\t\tm=m*10;\r\n\t}\r\n\treturn m;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tint a[100];\r\n\tscanf(\"%d\",&n);\r\n\tint sum=0;\r\n\tif(n>=0)\r\n\t{\r\n\t\tint i=0;\r\n\t\twhile(n!=0)\r\n\t\t{\r\n\t\t\ta[i]=n%10;\t\r\n\t\t\tn=n/10;\r\n\t\t\ti++;\r\n\t\t}\r\n\t\tint j=i;\r\n\t\tint z=0;\r\n\t\tfor(i=j-1;i>=0;i--,z++)\r\n\t\t{\r\n\t\t\tsum+=pos(10,i)*a[z];\r\n\t\t}\r\n\t}\r\n\telse\r\n\t{\r\n\t\tint i=0;\r\n\t\twhile(n!=0)\r\n\t\t{\r\n\t\t\ta[i]=n%10;\t\r\n\t\t\tn=n/10;\r\n\t\t\ti++;\r\n\t\t}\r\n\t\tint j=i;\r\n\t\tint z=0;\r\n\t\tfor(i=j-1;i>=0;i--,z++)\r\n\t\t{\r\n\t\t\tsum+=pos(10,i)*a[z];\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "2690": {
    "sid": 2480047,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tgets(a);\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tchar b[1000];\r\n\tint i,j=0;\r\n\tchar c[1000];\r\n\tm=m-1;\r\n\tif(strlen(a)>=m+n)\r\n\t{\r\n\t\tfor(i=m+n;i<strlen(a);i++)\r\n\t\t{\r\n\t\t\tb[j]=a[i];\r\n\t\t\tj++;\r\n\t\t}\r\n\t\tb[j]='\\0';\r\n\t\tfor(i=0;i<m;i++)\r\n\t\t{\r\n\t\t\tc[i]=a[i];\r\n\t\t}\r\n\t\tc[i]='\\0';\r\n\t\tstrcat(c,b);\r\n\t\tputs(c);\r\n\t}\r\n\telse\r\n\t{\r\n\t\tprintf(\"Illegal input\");\r\n\t}\r\n}"
  },
  "2776": {
    "sid": 2480046,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100][100];\r\n\tint i;\r\n\tfor(i=0;i<6;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t}\r\n\tint j;\r\n\tfor(i=0;i<6;i++)\r\n\t{\r\n\t\tfor(j=0;j<strlen(a[i]);j++)\r\n\t\t{\r\n\t\t\tif(a[i][j]>='a'&&a[i][j]<='z')\r\n\t\t\t{\r\n\t\t\t\ta[i][j]=a[i][j]-32;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tchar t[100];\r\n\tfor(i=0;i<5;i++)\r\n\t{\r\n\t\tfor(j=0;j<5-i;j++)\r\n\t\t{\r\n\t\t\tif(strcmp(a[j],a[j+1])>0)\r\n\t\t\t{\r\n\t\t\t\tstrcpy(t,a[j]);\r\n\t\t\t\tstrcpy(a[j],a[j+1]);\r\n\t\t\t\tstrcpy(a[j+1],t);\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<6;i++)\r\n\t{\r\n\t\tfor(j=0;j<strlen(a[i]);j++)\r\n\t\t{\r\n\t\t\tprintf(\"%c\",a[i][j]);\r\n\t\t}\r\n\t\tif(i!=5)\r\n\t\tprintf(\"\\n\");\r\n\t}\r\n}"
  },
  "2775": {
    "sid": 2480044,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[1000];\r\n\tgets(a);\r\n\tint x=0,y=0,z=0,i;\r\n\tfor(i=0;i<strlen(a);i++)\r\n\t{\r\n\t\tif((a[i]>='A'&&a[i]<='Z')||(a[i]>='a'&&a[i]<='z'))\r\n\t\tx++;\r\n\t\telse if(a[i]>='0'&&a[i]<='9')\r\n\t\ty++;\r\n\t\telse\r\n\t\tz++;\r\n\t}\r\n\tprintf(\"%d,%d,%d\",x,y,z);\r\n}"
  },
  "4225": {
    "sid": 2480042,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint a,b,c,d;\r\n\tint min=100;\r\n\tscanf(\"%d\",&n);\r\n\tfor(a=0;a<=n/64;a++)\r\n\t{\r\n\t\tfor(b=0;b<=n/27;b++)\r\n\t\t{\r\n\t\t\tfor(c=0;c<=n/8;c++)\r\n\t\t\t{\r\n\t\t\t\td=n-a*64-b*27-c*8;\r\n\t\t\t\tif(d>=0)\r\n\t\t\t\t{\r\n\t\t\t\t\tif(min>a+b+c+d)\r\n\t\t\t\t\t{\r\n\t\t\t\t\t\tmin=a+b+c+d;\r\n\t\t\t\t\t}\r\n\t\t\t\t}\t\t\t\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",min);\r\n}"
  },
  "4243": {
    "sid": 2480041,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tprintf(\"FFTT\");\r\n}"
  },
  "4244": {
    "sid": 2480040,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tint a[m][n];\r\n\tint i,j;\r\n\tint sum=0;\r\n\tfor(i=0;i<m;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t\tsum=sum+a[i][j];\r\n\t\t}\r\n\t}\r\n\tint f;\r\n\tif(sum%2==0)\r\n\t{\r\n\t\tf=m*n;\r\n\t\tprintf(\"%d\",f);\r\n\t}\r\n\telse\r\n\t{\r\n\t\tf=m*n-1;\r\n\t\tprintf(\"%d\",f);\r\n\t}\r\n}"
  },
  "4246": {
    "sid": 2480039,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tint i;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tif(m%2==0)\r\n\t\tm=m-i;\r\n\t\telse\r\n\t\tm=m+i;\r\n\t}\r\n\tprintf(\"%d\",m);\r\n} "
  },
  "4247": {
    "sid": 2480038,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[10000];\r\n\tint i;\r\n\tgets(a);\r\n\tfor(i=0;i<strlen(a)-2;i++)\r\n\t{\r\n\t\tif(a[i+1]-a[i]==6&&a[i+1]-a[i+2]==6)\r\n\t\t{\r\n\t\t\tprintf(\"Yes\");\r\n\t\t\treturn 0;\r\n\t\t}\r\n\t\telse if(a[i+1]-a[i]==-20&&a[i+1]-a[i+2]==-20)\r\n\t\t{\r\n\t\t\tprintf(\"Yes\");\r\n\t\t\treturn 0;\r\n\t\t}\r\n\t}\r\n\tprintf(\"No\");\r\n\treturn 0;\r\n}"
  },
  "4248": {
    "sid": 2480037,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint x,y,z;\r\n\tint x1,y1,z1;\r\n\tscanf(\"%d%d%d\",&x,&y,&z);\r\n\tscanf(\"%d%d%d\",&x1,&y1,&z1);\r\n\tint L=2,L1=2; \t\r\n\tL=L+z;\r\n\tL1=L1+z1;\r\n\tint g,g1;\r\n\twhile(1)\r\n\t{\r\n\t\tx=x+1;\r\n\t\tif(x<=3)\r\n\t\t{\r\n\t\t\tif(y1>=x)\r\n\t\t\t{\r\n\t\t\t\ty1=y1-x;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tx=x-y1;\r\n\t\t\t\ty1=0;\t\r\n\t\t\t\tL1=L1-x;\r\n\t\t\t}\r\n\t\t\tx=0;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tg=3;\r\n\t\t\tif(y>=g)\r\n\t\t\t{\r\n\t\t\t\ty1=y1-g;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tg=g-y1;\r\n\t\t\t\ty1=0;\t\r\n\t\t\t\tL1=L1-g;\r\n\t\t\t}\r\n\t\t\tx=x-3;\r\n\t\t}\r\n\t\tif(L1<=0)\r\n\t\t{\r\n\t\t\tprintf(\"A\");\r\n\t\t\treturn 0;\r\n\t\t}\r\n\t\tx1=x1+1;\r\n\t\tif(x1<=3)\r\n\t\t{\r\n\t\t\tif(y>=x1)\r\n\t\t\t{\r\n\t\t\t\ty=y-x1;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tx1=x1-y;\r\n\t\t\t\ty=0;\t\r\n\t\t\t\tL=L-x1;\r\n\t\t\t}\r\n\t\t\tx1=0;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tg=3;\r\n\t\t\tif(y>=g)\r\n\t\t\t{\r\n\t\t\t\ty=y-g;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\tg=g-y;\r\n\t\t\t\ty=0;\t\r\n\t\t\t\tL=L-g;\r\n\t\t\t}\r\n\t\t\tx1=x1-3;\r\n\t\t}\r\n\t\tif(L<=0)\r\n\t\t{\r\n\t\t\tprintf(\"B\");\r\n\t\t\treturn 0;\r\n\t\t}\r\n\t}\t\r\n}"
  },
  "3812": {
    "sid": 2480033,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main() \r\n{\r\n\tint i;\r\n\tchar a[100][100];\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tgetchar();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tgets(a[i]);\r\n\t} \r\n\tint max;\r\n\tmax=strlen(a[0]);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(max<strlen(a[i]))\r\n\t\t{\r\n\t\t\tmax=strlen(a[i]);\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",max);\r\n}"
  },
  "3885": {
    "sid": 2480032,
    "code": "C++",
    "content": "#include <stdio.h>\r\n#include <string.h>\r\nint main()\r\n{\r\n\tint n,j=0,i,t;\r\n\tchar s[10][20];\r\n\tscanf(\"%d\\n\",&n);\r\n\tfor(i=0;i<n;i++)\r\n\tscanf(\"%s\",&s[i]);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tt=strcmp(s[j],s[i]);\r\n\t\tif(t>0)\r\n\t\tj=i;\r\n\t}\r\n\tprintf(\"%s\",s[j]);\r\n}"
  },
  "3779": {
    "sid": 2480030,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a,b,c;\r\n\tscanf(\"%d/%d/%d\",&a,&b,&c);\r\n\tint day=0;\r\n\tint i;\r\n\tint tem=0;\r\n\tif(a>1982)\r\n\t{\r\n\t\tfor(i=1982;i<a;i++)\r\n\t\t{\r\n\t\t\tday=day+365;\r\n\t\t\tif(i%4==0&&i%100!=0||i%400==0)\r\n\t\t\t{\r\n\t\t\t\tday++;\r\n\t\t\t}\r\n\t\t}\r\n\t\tswitch(b)\r\n\t\t{\r\n\t\t\tcase 12:day=day+30;\r\n\t\t\tcase 11:day=day+31;\r\n\t\t\tcase 10:day=day+30;\r\n\t\t\tcase 9:day=day+31;\r\n\t\t\tcase 8:day=day+31;\r\n\t\t\tcase 7:day=day+30;\r\n\t\t\tcase 6:day=day+31;\r\n\t\t\tcase 5:day=day+30;\r\n\t\t\tcase 4:day=day+31;\r\n\t\t\tcase 3:day=day+28;\r\n\t\t\tcase 2:day=day+31;\r\n\t\t\tcase 1:day=day+c-1;\r\n\t\t}\r\n\t\t\r\n\t\tif((a%4==0&&a%100!=0||a%400==0)&&b>=3)\r\n\t\tday++;\r\n\t\tday=day+54;\r\n\t} \r\n\telse if(a==1982)\r\n\t{\r\n\t\tif(b>11)\r\n\t\t{\r\n\t\t\tday=day+23+c;\r\n\t\t}\r\n\t\telse if(b==11)\r\n\t\t{\r\n\t\t\tif(c>7)\r\n\t\t\tday=day+(c-7);\r\n\t\t\telse if(c==7)\r\n\t\t\tday=0;\r\n\t\t\telse\r\n\t\t\tday=day-(7-c);\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tswitch(b)\r\n\t\t\t{\r\n\t\t\t\tcase 12:tem=tem+30;\r\n\t\t\t\tcase 11:tem=tem+31;\r\n\t\t\t\tcase 10:tem=tem+30;\r\n\t\t\t\tcase 9:tem=tem+31;\r\n\t\t\t\tcase 8:tem=tem+31;\r\n\t\t\t\tcase 7:tem=tem+30;\r\n\t\t\t\tcase 6:tem=tem+31;\r\n\t\t\t\tcase 5:tem=tem+30;\r\n\t\t\t\tcase 4:tem=tem+31;\r\n\t\t\t\tcase 3:tem=tem+28;\r\n\t\t\t\tcase 2:tem=tem+31;\r\n\t\t\t\tcase 1:tem=tem+c;\r\n\t\t\t}\r\n\t\t\t\r\n\t\t\tif((a%4==0&&a%100!=0||a%400==0)&&b>=3)\r\n\t\t\ttem++;\r\n\t\t\tday=day-(311-tem);\r\n\t\t}\r\n\t}\r\n\telse\r\n\t{\r\n\t\t\tfor(i=a;i<1982;i++)\r\n\t\t\t{\r\n\t\t\t\tday=day-365;\r\n\t\t\t\tif(i%4==0&&i%100!=0||i%400==0)\r\n\t\t\t\tday--;\r\n\t\t\t}\r\n\t\t\tswitch(b)\r\n\t\t\t{\r\n\t\t\t\tcase 12:tem=tem+30;\r\n\t\t\t\tcase 11:tem=tem+31;\r\n\t\t\t\tcase 10:tem=tem+30;\r\n\t\t\t\tcase 9:tem=tem+31;\r\n\t\t\t\tcase 8:tem=tem+31;\r\n\t\t\t\tcase 7:tem=tem+30;\r\n\t\t\t\tcase 6:tem=tem+31;\r\n\t\t\t\tcase 5:tem=tem+30;\r\n\t\t\t\tcase 4:tem=tem+31;\r\n\t\t\t\tcase 3:tem=tem+28;\r\n\t\t\t\tcase 2:tem=tem+31;\r\n\t\t\t\tcase 1:tem=tem+c+1;\r\n\t\t\t}\r\n\t\t\tif((a%4==0&&a%100!=0||a%400==0)&&b>=3)\r\n\t\t\t{\r\n\t\t\t\ttem++;\r\n\t\t\t}\r\n\t\t\tif(a%4==0&&a%100!=0||a%400==0)\r\n\t\t\t{\r\n\t\t\t\ttem=(366-tem);\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t{\r\n\t\t\t\ttem=(365-tem);\r\n\t\t\t}\r\n\t\t\tday=day-311-tem;\r\n\t}\r\n\tint f=0;\r\n\tif(day>0)\r\n\t{\r\n\t\tday=day%7;\r\n\t\tswitch(day)\r\n\t\t{\r\n\t\t\tcase 0:f=7;break;\r\n\t\t\tcase 1:f=1;break;\r\n\t\t\tcase 2:f=2;break;\r\n\t\t\tcase 3:f=3;break;\r\n\t\t\tcase 4:f=4;break;\r\n\t\t\tcase 5:f=5;break;\r\n\t\t\tcase 6:f=6;break;\r\n\t\t}\r\n\t}\r\n\telse if(day==0)\r\n\t{\r\n\t\tf=7;\r\n\t}\r\n\telse\r\n\t{\r\n\t\tday=-day;\r\n\t\tday=day%7;\r\n\t\tswitch(day)\r\n\t\t{\r\n\t\t\tcase 0:f=7;break;\r\n\t\t\tcase 1:f=6;break;\r\n\t\t\tcase 2:f=5;break;\r\n\t\t\tcase 3:f=4;break;\r\n\t\t\tcase 4:f=3;break;\r\n\t\t\tcase 5:f=2;break;\r\n\t\t\tcase 6:f=1;break;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",f);\r\n}"
  },
  "2714": {
    "sid": 2480024,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,m;\r\n\tint i,j;\r\n\tint min[100];\r\n\tint max[100];\r\n\tint a[100][100];\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tscanf(\"%d\",&a[i][j]);\r\n\t\t}\r\n\t}\r\n\tint M;\r\n\tint N;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tN=a[i][0];\r\n\t\tfor(j=0;j<n;j++)\r\n\t\t{\r\n\t\t\tif(N>a[i][j])\r\n\t\t\tN=a[i][j];\r\n\t\t} \r\n\t\tmin[i]=N;\r\n\t}\r\n\tfor(j=0;j<n;j++)\r\n\t{\r\n\t\tM=a[0][j];\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tif(M<a[i][j])\r\n\t\t\tM=a[i][j];\r\n\t\t}\r\n\t\tmax[j]=M;\r\n\t}\r\n\tj=0;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tif(min[i]==max[i])\r\n\t\t{\r\n\t\t\tif(j==0)\r\n\t\t\tprintf(\"%d\",min[i]);\r\n\t\t\telse\r\n\t\t\tprintf(\" %d\",min[i]);\r\n\t\t\tj++;\r\n\t\t}\t\r\n\t}\r\n}"
  },
  "2715": {
    "sid": 2480023,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tint a[10000];\r\n\tint i;\r\n\tfor(i=0;i<n;i++)\r\n\tscanf(\"%d\",&a[i]);\r\n\tint max=1;\r\n\tint tem=0;\r\n\tint s;\r\n\ts=a[0];\r\n\tfor(i=0;i<n;i++)\r\n\t{\t\r\n\t\tif(s==a[i])\r\n\t\ttem++;\r\n\t\telse\r\n\t\t{\r\n\t\t\tif(tem>max)\r\n\t\t\tmax=tem;\r\n\t\t\ttem=1;\r\n\t\t\ts=a[i];\r\n\t\t}\r\n\t\tif(i==n-1)\r\n\t\t{\r\n\t\t\tif(tem>max)\r\n\t\t\tmax=tem;\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d\",max);\r\n}"
  },
  "1552": {
    "sid": 2480022,
    "code": "Java",
    "content": "import java.util.Scanner;\r\nclass Main\r\n{\r\n\tpublic static void main(String args[])\r\n\t{\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint i,j=0,z=1;\r\n\t\tint a1,b1;\r\n\t\twhile(true)\r\n\t\t{\r\n\t\t\tint a=input.nextInt();\r\n\t\t\tint b=input.nextInt();\r\n\t\t\tint k=input.nextInt();\r\n\t\t\tif(a==0&&b==0)\r\n\t\t\t\tbreak;\r\n\t\t\tz=1;\r\n\t\t\tfor(i=0;i<k;i++)\r\n\t\t\t{\r\n\t\t\t\tz=z*10;\r\n\t\t\t}\r\n\t\t\ta1=a%z;\r\n\t\t\twhile(a1>=10)\r\n\t\t\t{\r\n\t\t\t\ta1=a1/10;\r\n\t\t\t}\r\n\t\t\tb1=b%z;\r\n\t\t\twhile(b1>=10)\r\n\t\t\t{\r\n\t\t\t\tb1=b1/10;\r\n\t\t\t}\r\n\t\t\tif(a1==b1)\r\n\t\t\t\tSystem.out.println(-1);\r\n\t\t\telse\r\n\t\t\t\tSystem.out.println(a+b);\r\n\t\t}\r\n\t}\r\n}"
  },
  "1554": {
    "sid": 2480021,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tif(n==1)\r\n\t\treturn 1;\r\n\telse\r\n\t\treturn fac(n-1)+n;\r\n}\r\nint main()\r\n{\r\n\tint f=0;\r\n\tint s=0;\r\n\tint a,b;\r\n\tchar c;\r\n\twhile(1)\r\n\t{\t\r\n\t\tscanf(\"%d%c%d\",&a,&c,&b);\r\n\t\tif(a==0&&b==0)\r\n\t\t\tbreak;\r\n\t\tif(a==7)\r\n\t\t\tf=b;\r\n\t\tif(a==8)\r\n\t\t\tf=31+b;\r\n\t\tint i;\r\n\t\tint j=0;\r\n\t\tfor(i=1;i<11;i++)\r\n\t\t{\r\n\t\t\tif(f<=fac(i))\r\n\t\t\t\tj++;\r\n\t\t}\r\n\t\tprintf(\"%d\\n\",j);\r\n\t}\t\t\r\n}"
  },
  "2773": {
    "sid": 2480020,
    "code": "Java",
    "content": "class Main\r\n{\r\n    public static void main(String[] args)\r\n\t{\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint n=input.nextInt();\r\n\t\tint i;\r\n\t\tint sum=0;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tint a=input.nextInt();\r\n\t\t\tif(a%3==0)\r\n\t\t\t\tsum=sum+a;\r\n\t\t}\r\n\t\tSystem.out.print(sum);\r\n\t}\r\n}"
  },
  "1550": {
    "sid": 2480019,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tstruct man{\r\n\t\tchar hao[10];\r\n\t\tchar name[16];\r\n\t\tint a;\r\n\t\tint b;\r\n\t\tint c;\r\n\t}s[n];\r\n\tint sum=0,max,z1=0,z2=0,z3=0;\r\n\tint j,i;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%s %s %d %d %d\",&s[i].hao,&s[i].name,&s[i].a,&s[i].b,&s[i].c);\r\n\t\tz1=z1+s[i].a;\r\n\t\tz2=z2+s[i].b;\r\n\t\tz3=z3+s[i].c;\r\n\t\tif(i==0)\r\n\t\t{\r\n\t\t\tsum=s[i].a+s[i].b+s[i].c;\r\n\t\t\tj=i;\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tmax=s[i].a+s[i].b+s[i].c;\r\n\t\t\tif(sum<max)\r\n\t\t\t{\r\n\t\t\t\tsum=max;\r\n\t\t\t\tj=i;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tprintf(\"%d %d %d\\n\",z1/n,z2/n,z3/n);\r\n\tprintf(\"%s %s %d %d %d\",s[j].hao,s[j].name,s[j].a,s[j].b,s[j].c);\r\n\t\r\n}"
  },
  "1942": {
    "sid": 2480017,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int n)\r\n{\r\n\tif(n==1)\r\n\treturn 0;\r\n\tint i;\r\n\tfor(i=2;i<=(n+1)/2;i++)\r\n\t{\r\n\t\tif(n%i==0)\r\n\t\treturn 0;\r\n\t}\r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint i;\r\n\tint m,n;\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tint sum=0;\r\n\tfor(i=m;i<=n;i++)\r\n\t{\r\n\t\tif(fac(i)==1)\r\n\t\tsum=sum+i;\r\n\t} \r\n\tprintf(\"%d\",sum);\r\n}"
  },
  "1858": {
    "sid": 2480011,
    "code": "Java",
    "content": "import java.util.Scanner;\r\nclass Main\r\n{\r\n\tpublic static void main(String args[])\r\n\t{\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint n=input.nextInt();\r\n\t\tint i;\r\n\t\tint j;\r\n\t\tint z;\r\n\t\tfor(i=0;i<n;i++)\r\n\t\t{\r\n\t\t\tfor(j=2*(n-i-1);j>0;j--)\r\n\t\t\t{\r\n\t\t\t\tSystem.out.print(\" \");\r\n\t\t\t}\r\n\t\t\tSystem.out.print(\"*\");\r\n\t\t\tif(i!=0)\r\n\t\t\t{\r\n\t\t\t\tfor(z=0;z<4*i-1;z++)\r\n\t\t\t\t{\r\n\t\t\t\t\tSystem.out.print(\" \");\r\n\t\t\t\t}\r\n\t\t\t\tSystem.out.print(\"*\");\r\n\t\t\t}\r\n\t\t\tSystem.out.print(\"\\n\");\r\n\t\t}\r\n\t\tfor(i=0;i<n-1;i++)\r\n\t\t{\r\n\t\t\tfor(j=0;j<2*(i+1);j++)\r\n\t\t\t{\r\n\t\t\t\tSystem.out.print(\" \");\r\n\t\t\t}\r\n\t\t\tSystem.out.print(\"*\");\r\n\t\t\tif(i!=n-2)\r\n\t\t\t{\r\n\t\t\t\tfor(j=4*(n-i-2)-2;j>=0;j--)\r\n\t\t\t\t{\r\n\t\t\t\t\tSystem.out.print(\" \");\r\n\t\t\t\t}\r\n\t\t\t\tSystem.out.print(\"*\");\r\n\t\t\t}\r\n\t\t\tSystem.out.print(\"\\n\");\t\r\n\t\t}\r\n\t}\r\n}"
  },
  "3874": {
    "sid": 2480006,
    "code": "Java",
    "content": "import java.util.Scanner;\r\nclass Main\r\n{\r\n\tpublic static void main(String args[])\r\n\t{\r\n\t\t/*java.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint n=input.nextInt();*/\r\n\t\tint i;\r\n\t\tint sum=0;\r\n\t\tint j=1;\r\n\t\tfor(i=0;i<8;i++)\r\n\t\t{\r\n\t\t\tsum=sum+j;\r\n\t\t\tj=j*2;\r\n\t\t}\r\n\t\tint n;\r\n\t\tn=765/sum;\r\n\t\tint m=n;\r\n\t\tfor(i=0;i<7;i++)\r\n\t\t{\r\n\t\t\tm=m*2;\r\n\t\t}\r\n\t\tSystem.out.print(n+\" \"+m);\r\n\t}\r\n}"
  },
  "1934": {
    "sid": 2480005,
    "code": "C++",
    "content": "#include <iostream>   \r\nusing namespace std;  \r\n  \r\nint main()  \r\n{  \r\n    char str[10000];  \r\n   int count = 0, i;  \r\n \r\n   while (gets(str))  \r\n    {  \r\n       i = 0;  \r\n        if (str[0] == '\\0')  \r\n          break;  \r\n       while (str[i])  \r\n        {  \r\n           if (str[i] == '$')  \r\n               count++;  \r\n           i++;  \r\n        }  \r\n    }  \r\n    cout << count;  \r\n   return 0;  \r\n}  \r\n"
  },
  "3787": {
    "sid": 2480004,
    "code": "Java",
    "content": "class Main {\r\n\r\n\tpublic static void main(String[] args) {\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint n=input.nextInt();\r\n\t\tif(n>=1&&n<100&&n%2==1)\r\n\t\t{\r\n\t\t\tint sum=0;\r\n\t\t\tint i=1;\r\n\t\t\twhile(true)\r\n\t\t\t{\r\n\t\t\t\tsum=sum+i;\r\n\t\t\t\tif(i==n)\r\n\t\t\t\tbreak;\r\n\t\t\t\ti=i+2;\t\r\n\t\t\t}\r\n\t\t\tSystem.out.print(sum);\r\n\t\t}\r\n\t\telse\r\n\t\t{\r\n\t\t\tSystem.out.print(\"error\");\r\n\t\t}\r\n\t}\r\n\r\n}"
  },
  "3839": {
    "sid": 2480003,
    "code": "C",
    "content": "#include<stdio.h>\r\nint fac(int a)\r\n{\r\n\tif(a==1||a==2||a==3)\r\n\treturn 2;\r\n\telse\r\n\treturn fac(a-1)*fac(a-2)*fac(a-3);\r\n}\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\tprintf(\"%d\",fac(a));\r\n} "
  },
  "1559": {
    "sid": 2480002,
    "code": "Java",
    "content": "class Main {\r\n\tpublic static int fac(int n)\r\n\t{\r\n\t\tif(n==1)\r\n\t\t\treturn 1;\r\n\t\telse if(n==2)\r\n\t\t\treturn 2;\r\n\t\telse\r\n\t\t\treturn fac(n-1)+fac(n-2);\r\n\t}\r\n\tpublic static void main(String[] args) {\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\twhile(true)\r\n\t\t{\r\n\t\t\tint n=input.nextInt();\r\n\t\t\tif(n==0)\r\n\t\t\t\tbreak;\r\n\t\t\tSystem.out.println(fac(n));\r\n\t\t}\r\n\t}\r\n}\r\n"
  },
  "1022": {
    "sid": 2480001,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\n#include<stdlib.h>\r\nint main()\r\n{\r\n\tint a[10000];\r\n\tint buffer[10000];\r\n\tint i;\r\n\tint j;\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t    int id = 0;\r\n        for(int i = 0; i<n; i++)\r\n        {\r\n            scanf(\"%d\", &a[i]);\r\n            if(i)\r\n\t\t\tbuffer[id++] = abs(a[i]-a[i-1]);\r\n        }\r\n        int t;\r\n        for(i=0;i<n-2;i++)\r\n        {\r\n    \t\tfor(j=0;j<n-2-i;j++)\r\n    \t\t{\r\n\t        \tif(buffer[j]>buffer[j+1])\r\n\t        \t{\r\n        \t\t\tt=buffer[j];\r\n        \t\t\tbuffer[j]=buffer[j+1];\r\n\t\t\t\t\tbuffer[j+1]=t; \r\n        \t\t}\r\n\t        }\r\n    \t}\r\n        int flag = 1;\r\n        for(int i = 0; i<id; i++)\r\n        {\r\n            if(buffer[i] != i+1)\r\n            {\r\n                flag = 0;\r\n                break;\r\n            }\r\n        }\r\n        if(flag)\r\n\t\tprintf(\"Jolly\\n\");\r\n        else\r\n\t\tprintf(\"Not jolly\\n\");\r\n    }\r\n\treturn 0;\r\n} "
  },
  "1547": {
    "sid": 2480000,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n,m;\r\n\tscanf(\"%d\",&n);\r\n\tchar a[1000];\r\n\tint i;\r\n\tgetchar();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%c\",&a[i]);\r\n\t}\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=m-1;i<n;i++)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n} "
  },
  "3887": {
    "sid": 2479998,
    "code": "C",
    "content": "#include<stdio.h>\n#include<stdio.h>\n#include<stdio.h> \r\nint main()\r\n{\r\n\tstruct man {\r\n\t\tint xue;\r\n\t\tint grade;\r\n\t\tchar name[20];\r\n\t};\r\n\tint n;\r\n\tscanf(\"%d\", &n);\r\n\tstruct man s[1000];\r\n\tint i;\r\n\tfor (i = 0; i < n; i++)\r\n\t{\r\n\t\tscanf(\"%d,%d,%s\", &s[i].xue, &s[i].grade, s[i].name);\r\n\t}\r\n\tfor (i = 0; i <= n - 1; i++)\r\n\t\tif (s[i].grade >= 60)\r\n\t\t{\r\n\t\t\tprintf(\"%d,%d,%s\\n\", s[i].xue, s[i].grade, s[i].name);\r\n\t\t}\r\n\r\n\treturn 0;\r\n}\r\n\r\n"
  },
  "2069": {
    "sid": 2479997,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct Node\r\n{\r\n    int data;   \r\n   struct Node *next;\r\n}LNode,*LinkList;\r\nLinkList createList()\r\n{\r\n\tLinkList headNode=(LinkList)malloc(sizeof(LNode));\r\n\theadNode->next=headNode;\r\n}\r\nLinkList createNode(int data)\r\n{\r\n\tLinkList posNode=(LinkList)malloc(sizeof(LNode));\r\n\tposNode->data=data;\r\n\tposNode->next=NULL;\r\n}\r\n/*void dingdian(LinkList headNode,int data,int position)\r\n{\r\n\tLinkList newNode=createNode(data);\r\n\tLinkList posnode=headNode->next;\r\n\tLinkList posfront=headNode;\r\n\twhile(--position)\r\n\t{\r\n\t\tposfront=posfront->next;\r\n\t\tposnode=posfront->next;\r\n\t} \r\n\tnewNode->next=posnode;\r\n\tposfront->next=newNode;\r\n}*/\r\nvoid dingdian(LinkList headNode,int data,int position)\r\n{\r\n\tLinkList newNode=createNode(data);\r\n\tLinkList posnode=headNode;\r\n\twhile(--position)\r\n\t{\r\n\t\tposnode=posnode->next;\r\n\t} \r\n\tnewNode->next=posnode->next;\r\n\tposnode->next=newNode;\r\n}\r\nvoid printList(LinkList headNode)\r\n{\r\n\tLinkList pMove=headNode->next;\r\n\tint i=0;\r\n\twhile(pMove!=headNode)\r\n\t{\r\n\t\tprintf(\"%d \",pMove->data);\r\n\t\ti++;\r\n\t\tpMove=pMove->next;\r\n\t}\r\n}\r\nvoid chaji(LinkList A,LinkList B,LinkList C,int n,int m)\r\n{\r\n\tLinkList amove=A->next;\r\n\tLinkList bmove=B->next;\r\n\tint i;\r\n\tint j;\r\n\tint z=1;\r\n\tint k;\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tk=0;\r\n\t\tfor(j=1;j<=m;j++)\r\n\t\t{\r\n\t\t\tif(amove->data==bmove->data)\r\n\t\t\t{\r\n\t\t\t\tk++;\r\n\t\t\t}\r\n\t\t\tbmove=bmove->next; \r\n\t\t}\r\n\t\tif(k==0)\r\n\t\t{\r\n\t\t\tdingdian(C,amove->data,z);\r\n\t\t\tz++;\r\n\t\t}\r\n\t \tbmove=B->next;\r\n\t\tamove=amove->next;\r\n\t}\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\tint i;\r\n\tint a,b,c;\r\n\tLinkList A=createList();\r\n\tLinkList B=createList();\r\n\tLinkList C=createList();\r\n\tscanf(\"%d\",&n);\r\n\tfor(i=1;i<=n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a);\r\n\t\tdingdian(A,a,i);\r\n\t}\r\n\tint m;\r\n\tscanf(\"%d\",&m);\r\n\tfor(i=1;i<=m;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&b);\r\n\t\tdingdian(B,b,i);\r\n\t}\r\n\tchaji(A,B,C,n,m);\r\n\tprintList(C);\r\n}"
  },
  "2609": {
    "sid": 2479996,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\n#include<stdlib.h>\r\n#include<math.h>\r\ntypedef struct Data{\r\n\tint data;\r\n\tstruct Data *next;\r\n}LNode,*LinkList;\r\nLinkList createList()\r\n{\r\n\tLinkList headNode=(LinkList)malloc(sizeof(LNode));\r\n\theadNode->next=NULL;\r\n\treturn headNode;\r\n}\r\nLinkList createNode(int data)\r\n{\r\n\tLinkList posNode=(LinkList)malloc(sizeof(LNode));\r\n\tposNode->data=data;\r\n\tposNode->next=NULL;\r\n}\r\nvoid insert(int data,LinkList headNode)\r\n{\r\n\tLinkList posNode=(LinkList)malloc(sizeof(LNode));\r\n\tposNode=createNode(data);\r\n\tposNode->next=headNode->next;\r\n\theadNode->next=posNode;\t\r\n}\r\nvoid printList(LinkList headNode)\r\n{\r\n\tint i=0;\r\n\tLinkList posNode=headNode->next;\r\n\twhile(posNode!=NULL)\r\n\t{\t\r\n\t    if(i==0)\r\n\t\tprintf(\"%d\",posNode->data);\r\n\t\telse\r\n\t\tprintf(\" %d\",posNode->data);\r\n\t\tposNode=posNode->next;\r\n\t\ti++;\r\n\t} \r\n} \r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"m=%d\",&n);\r\n\tint i;\r\n\tint j;\r\n\tint a[1000];\r\n\tLinkList headNode=createList();\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tscanf(\"%d\",&a[i]);\r\n\t}\r\n\tint t;\r\n\tfor(i=0;i<n-1;i++)\r\n\t{\r\n\t\tfor(j=0;j<n-i-1;j++)\r\n\t\t{\r\n\t\t\tif(a[j]<a[j+1])\r\n\t\t\t{\r\n\t\t\t\tt=a[j];\r\n\t\t\t\ta[j]=a[j+1];\r\n\t\t\t\ta[j+1]=t;\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tinsert(a[i],headNode);\r\n\t}\r\n\tprintList(headNode);\r\n} "
  },
  "3044": {
    "sid": 2479981,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a[32]={0};\r\n\tint b;\r\n\tint i=0;\r\n\tscanf(\"%d\",&b);\r\n\twhile(b!=0)\r\n\t{\r\n\t\ta[i]=b%2;\r\n\t\tb=b/2;\r\n\t\ti++;\r\n\t}\r\n\tfor(i=31;i>=0;i--)\r\n\t{\r\n\t\tprintf(\"%d\",a[i]);\r\n\t}\r\n}"
  },
  "5308": {
    "sid": 2479980,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint a;\r\n\tscanf(\"%d\",&a);\r\n\ta&=1;\r\n\tprintf(\"%d\",a);\r\n} "
  },
  "2658": {
    "sid": 2479979,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[100];\r\n\tgets(a);\r\n\tfor(int i=2;i<strlen(a);i++)\r\n\t{\r\n\t\tprintf(\"%c\",a[i]);\r\n\t}\r\n\tprintf(\"%c%c\",a[0],a[1]);\r\n}"
  },
  "2640": {
    "sid": 2479978,
    "code": "Java",
    "content": "class Main{\r\n\tpublic static void main(String[] args)\r\n\t{\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint a=input.nextInt();\r\n\t\tSystem.out.println(Integer.toOctalString(a));\r\n\t}\r\n}\r\n"
  },
  "3742": {
    "sid": 2479977,
    "code": "Java",
    "content": "class Main{\r\n\tpublic static void main(String[] args)\r\n\t{\r\n\t\tjava.util.Scanner input=new java.util.Scanner(System.in);\r\n\t\tint a=input.nextInt();\r\n\t\tString s=String.valueOf(Integer.toBinaryString(a));\r\n\t\tint j=0;\r\n\t\tint number=0;\r\n\t\tfor(int i=0;i<s.length();i++) {\r\n\t\t\tj=Integer.parseInt(String.valueOf(s.charAt(i)));\r\n\t\t\tif(j==1)\r\n\t\t\t{\r\n\t\t\t\tnumber++;\r\n\t\t\t}\r\n\t\t}\r\n\t\tSystem.out.println(number);\r\n\t}\r\n}"
  },
  "3093": {
    "sid": 2479976,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tchar a[100],b[100],c[100];\r\n\tgetchar();\r\n\tscanf(\"%s\",&a);\r\n\tgetchar();\r\n\tscanf(\"%s\",&b);\r\n\tint i,j,i1;\r\n\tfor(i=0;i<n;i++)\r\n\t{\r\n\t\tc[i]=a[i];\r\n\t}\r\n\tfor(i1=i,j=0;b[j]!='\\0';j++,i1++)\r\n\t{\r\n\t\tc[i1]=b[j];\r\n\t} \r\n\tfor(;a[i]!='\\0';i1++,i++)\r\n\t{\r\n\t\tc[i1]=a[i];\r\n\t}\r\n\tc[i1]='\\0';\r\n\tputs(c);\r\n}"
  },
  "1873": {
    "sid": 2479974,
    "code": "Java",
    "content": "class Main{\r\n\tpublic static void main(String[] args)\r\n\t{\r\n\t\tSystem.out.println(\"This is a C program.\");\r\n\t}\r\n}"
  },
  "1923": {
    "sid": 2479973,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main()\r\n{\r\n\tchar a[3][100];\r\n\tscanf(\"%s %s %s\",&a[0],&a[1],&a[2]);\r\n\tchar t[100];\r\n\tfor(int i=0;i<2;i++)\r\n\t{\r\n\t\tfor(int j=0;j<2-i;j++)\r\n\t\t{\r\n\t\t\tif(strcmp(a[j],a[j+1])>0)\r\n\t\t\t{\r\n\t\t\t\tstrcpy(t,a[j]);\r\n\t\t\t\tstrcpy(a[j],a[j+1]);\r\n\t\t\t\tstrcpy(a[j+1],t);\r\n\t\t\t}\r\n\t\t}\r\n\t}\t\r\n\tprintf(\"%s %s %s\",a[0],a[1],a[2]);\r\n}"
  },
  "1126": {
    "sid": 2479971,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tlong long int num[51];\r\n\tint n;\r\n\twhile (~scanf(\"%d\",&n)) {\r\n         num[1] = 1;\r\n         num[2] = 2;\r\n         for (int i = 3; i <= n; i++) {\r\n             num[i] = num[i - 1] + num[i - 2];\r\n         }\r\n         printf(\"%lld\\n\", num[n]);\r\n     }\r\n} "
  },
  "1134": {
    "sid": 2479970,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint fac(int n)\r\n{\r\n\tint i;\r\n\tfor(i=2;i<sqrt(n);i++)\r\n\t{\r\n\t\tif(n%i==0)\r\n\t\treturn 0;\r\n\t}\r\n\treturn 1;\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(~scanf(\"%d\",&n)){\r\n\t\tif(n/100==n%10&&fac(n)==1)\r\n\t\tprintf(\"Yes\\n\");\r\n\t\telse\r\n\t\tprintf(\"No\\n\");\r\n\t}\r\n}"
  },
  "1798": {
    "sid": 2479969,
    "code": "C++",
    "content": "#include <stdio.h>\r\n\r\n\r\n\r\nint leap(int a)                             \r\n\r\n{\r\n\r\n    if (a % 4 == 0 && a % 100 != 0 || a % 400 == 0)     \r\n\r\n        return 1;                            \r\n\r\n    else\r\n\r\n        return 0;                            \r\n\r\n}\r\n\r\n\r\n\r\nint number(int year, int m, int d)                    \r\n\r\n{\r\n\r\n    int sum = 0, i, j, k, a[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };     \r\n\r\n    int b[12] = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };               \r\n\r\n    if (leap(year) == 1)                 \r\n        for (i = 0; i < m - 1; i++)\r\n\r\n            sum += b[i];                \r\n\r\n    else\r\n\r\n        for (i = 0; i < m - 1; i++)\r\n\r\n            sum += a[i];                \r\n\r\n    for (j = 2000; j < year; j++)\r\n\r\n        if (leap(j) == 1)\r\n\r\n            sum += 366;                 \r\n\r\n        else\r\n\r\n            sum += 365;                     \r\n\r\n    sum += d;                      \r\n    return sum;                    \r\n\r\n}\r\n\r\n\r\n\r\nint main()\r\n\r\n{\r\n\r\n    int year, month, day, n;\r\n\r\n    scanf(\"%d%d%d\", &year, &month, &day);     \r\n\r\n    n = number(year, month, day);            \r\n\r\n    if ((n % 5) < 4 && (n % 5) > 0)          \r\n\r\n        printf(\"fishing\");\r\n\r\n    else\r\n\r\n        printf(\"basking\");\r\n\r\n}"
  },
  "2345": {
    "sid": 2479968,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tint f=1;\r\n\tscanf(\"%d\",&n);\r\n\tfor(int i=2;i<=n;i++)\r\n\t{\r\n\t\tf=f*i;\r\n\t\twhile(f%10==0)\r\n\t\t{\r\n\t\t\tf/=10;\r\n\t\t}\r\n\t\tf=f%1000;\r\n\t}\r\n\tf%=10;\r\n\tprintf(\"%d\",f);\r\n}\r\n"
  },
  "5310": {
    "sid": 2479967,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tn=n&65535;\r\n\tprintf(\"%d\",n);\r\n} \r\n"
  },
  "5309": {
    "sid": 2479966,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <limits.h>\r\n \r\nchar * to_binary_str(char * buffer, int value)\r\n{\r\n    int i;\r\n    \r\n    for (i = sizeof(int) * 8 - 1; i > -1; i--)\r\n        buffer[31 - i] = ((value >> i) & 1) + '0';\r\n    buffer[sizeof(int) * 8] = '\\0';\r\n    \r\n    return buffer;\r\n}\r\n \r\nint main()\r\n{\r\n    char buffer[33];\r\n    int n;\r\n    \r\n    scanf(\"%d\", &n);\r\n    \r\n    if (n >= 0) {\r\n        printf(\"%s\\n\", to_binary_str(buffer, n));\r\n    } else {\r\n        if (n == INT_MIN)\r\n            printf(\"1%s\\n\", to_binary_str(buffer, n));\r\n        else\r\n            printf(\"%s\\n\", to_binary_str(buffer, ~n + 1 | INT_MIN));\r\n    }\r\n    return 0;\r\n}"
  },
  "5313": {
    "sid": 2479965,
    "code": "C",
    "content": "#include <stdio.h>\r\n#include <limits.h>\r\n \r\nchar * to_binary_str(char * buffer, int value)\r\n{\r\n    int i;\r\n    \r\n    for (i = sizeof(int) * 8 - 1; i > -1; i--)\r\n        buffer[31 - i] = ((value >> i) & 1) + '0';\r\n    buffer[sizeof(int) * 8] = '\\0';\r\n    \r\n    return buffer;\r\n}\r\n \r\nint main()\r\n{\r\n    char buffer[33];\r\n    int n;\r\n    \r\n    scanf(\"%d\", &n);\r\n    printf(\"%s\\n\", to_binary_str(buffer, n));\r\n    return 0;\r\n}"
  },
  "4298": {
    "sid": 2479964,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct{\r\n\tint x;\r\n\tint y;\r\n}Node;\r\ntypedef struct{\r\n\tint len;\r\n\tNode node[10000];\r\n}LNode,*LinkList;\r\nint a[100][100];\r\nint m,n;\r\nNode begin, end;\r\nLinkList create()\r\n{\r\n\tLinkList head=(LinkList)malloc(sizeof(LNode));\r\n\thead->len=-1;\r\n\treturn head;\r\n}\r\nint fac(LinkList head, Node node) {\r\n\tif(node.x == end.x && node.y == end.y)\r\n\treturn 1; \r\n\telse{\r\n\t\ta[node.x][node.y] = 1;\r\n\t\tfor(int i = 0; i < 4; i++) {\r\n\t\t\tNode next;\r\n\t\t\tnext.x=node.x;\r\n\t\t\tnext.y=node.y;\t\r\n\t\t\tif(i==0)\r\n\t\t\tnext.x--;\r\n\t\t\telse if(i==1)\r\n\t\t\tnext.x++;\r\n\t\t\telse if(i==3)\r\n\t\t\tnext.y--;\r\n\t\t\telse\r\n\t\t\tnext.y++;\r\n\t\t\tif(a[next.x][next.y] == 0 && next.x >= 0 && next.x < m && next.y >= 0 && next.y < n)//\u5224\u65ad\u4e0b\u4e00\u6b65\u662f\u5426\u662f\u5899\u6216\u662f\u4e0b\u6807\u8d8a\u754c \r\n\t\t\t{\r\n\t\t\t\thead->node[++head->len] = next;//\u589e\u52a0\u4e00\u4e2a\u8282\u70b9 \r\n\t\t\t\tif(fac(head, next)) \r\n\t\t\t\t  return 1; \r\n\t\t\t\tif(head->len!=-1)\r\n\t\t\t\t  head->len--;//\u51cf\u5c11\u4e00\u4e2a\u8282\u70b9 \r\n\t\t\t}\r\n\t\t}\r\n\t\ta[node.x][node.y]=0;\r\n\t\treturn 0; \r\n\t}\r\n}\r\nint main()\r\n{\r\n\tscanf(\"%d%d\",&m,&n);\r\n \tscanf(\"%d%d%d%d\",&begin.x,&begin.y,&end.x,&end.y);\r\n \tfor(int i = 0; i < m; i++)\r\n\t\tfor(int j = 0; j < n; j++)\r\n\t\t\tscanf(\"%d\", &a[i][j]);\r\n\tLinkList head=create();\r\n\thead->node[++head->len] = begin;\r\n\tif(fac(head,begin))\r\n\tfor(int i = 0; i < head->len + 1; i++)\r\n\tprintf(\"(%d %d)\", head->node[i].x, head->node[i].y);\r\n\telse\r\n\tprintf(\"No Path!\");\r\n}"
  },
  "4297": {
    "sid": 2479963,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include<stdlib.h>\r\ntypedef struct{\r\n\tint x;\r\n\tint y;\r\n\tint step;\r\n}point;\r\ntypedef struct{\r\n\tpoint data[1000];\r\n\tint front;//\u51fa \r\n\tint rear;//\u5165 \r\n}queue,*Queue;\r\nQueue List;\r\nint a[100][100];\r\nint m,n;\r\nint bk;\r\nint Fstep=0;\r\npoint begin,end;\r\nvoid create()\r\n{\r\n\tList=(Queue)malloc(sizeof(queue));\r\n\tList->front=0;\r\n\tList->rear=0;\r\n}\r\nvoid enter(point tem){\r\n\tList->rear=List->rear%1000;\r\n\tList->data[List->rear++]=tem;\r\n\ta[tem.x][tem.y]=1;\t\t\r\n}\r\nvoid out(){\r\n\t++List->front%=1000;\t\r\n}\r\nint main()\r\n{\r\n\tscanf(\"%d%d\",&m,&n);\r\n\tfor(int i=0;i<m;i++)\r\n\t\tfor(int j=0;j<n;j++)\r\n\t\tscanf(\"%d\",&a[i][j]);\r\n\tscanf(\"%d%d%d%d\",&begin.x,&begin.y,&end.x,&end.y);\t\t\r\n\tbegin.step=0;\r\n\tcreate();\r\n\tenter(begin);\r\n\twhile(List->front!=List->rear)\r\n\t{\r\n\t\tint num=0;\r\n\t \tbk=0;\r\n\t\tint step=List->data[List->front].step;\r\n\t\tfor(int i=0;i<4;i++)\r\n\t\t{\r\n\t\t\tpoint next=List->data[List->front];\t\r\n\t\t\tif(i==0)\r\n\t\t\tnext.x--;\r\n\t\t\telse if(i==1)\r\n\t\t\tnext.x++;\r\n\t\t\telse if(i==2)\r\n\t\t\tnext.y--;\r\n\t\t\telse\r\n\t\t\tnext.y++;\r\n\t\t\tnext.step++;\r\n\t\t\tif(a[next.x][next.y] == 0 && next.x >= 0 && next.x < m && next.y >= 0 && next.y < n)\t\r\n\t\t\t{\r\n\t\t\t\tenter(next);\r\n\t\t\t\tif(next.x==end.x&&next.y==end.y)\r\n\t\t\t\t{\r\n\t\t\t\t\tbk++;\r\n\t\t\t\t\tFstep=next.step;\r\n\t\t\t\t\tbreak;\r\n\t\t\t\t}\r\n\t\t\t} \r\n\t\t}\r\n\t\tif(bk==1)\r\n\t\t\tbreak;\r\n\t\tout();\r\n\t}\r\n\tif(bk==1)\r\n\tprintf(\"%d\",Fstep);            \r\n\telse\r\n\tprintf(\"no path!\");\r\n}\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n"
  },
  "5311": {
    "sid": 2479962,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\tscanf(\"%d\",&n);\r\n\tif(!(n&2))\r\n\t\tn+=2;\r\n\tprintf(\"%d\",n);\r\n} "
  },
  "4296": {
    "sid": 2479961,
    "code": "C",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t\tif(n>100||n<0)\r\n\t\tprintf(\"Score is error!\\n\");\r\n\t\telse{\r\n\t\t\tif(n>=90)\r\n\t\t\tprintf(\"A\\n\");\r\n\t\t\telse if(n>=80)\r\n\t\t\tprintf(\"B\\n\");\r\n\t\t\telse if(n>=70)\r\n\t\t\tprintf(\"C\\n\");\r\n\t\t\telse if(n>=60)\r\n\t\t\tprintf(\"D\\n\");\r\n\t\t\telse\r\n\t\t\tprintf(\"E\\n\");\r\n\t\t}\r\n\t}\r\n} "
  },
  "4293": {
    "sid": 2479960,
    "code": "C",
    "content": "#include<stdio.h>\r\nint f[41];\r\nint main()\r\n{\r\n\tint n,m,i;\r\n\tf[1]=0;\r\n\tf[2]=1;\r\n\tf[3]=2;\r\n\tfor(i=4;i<41;i++)\r\n\t\tf[i]=f[i-1]+f[i-2];\r\n\tscanf(\"%d\",&n);\r\n\twhile(n--)\r\n\t{\r\n\t\tscanf(\"%d\",&m);\r\n\t\tprintf(\"%d\\n\",f[m]);\r\n\t}\r\n\treturn 0;\r\n}\r\n"
  },
  "1223": {
    "sid": 2479959,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint a[6542];\r\nint isPrime (int n) {\r\n\tif (n < 2) return 0; \r\n\tif (n == 2) return 1; \r\n\tif (n % 2 == 0) return 0;\r\n\tint sq = sqrt(n);\r\n\tfor (int i = 3; i <= sq; i += 2) {\r\n\t\tif (n % i == 0) \r\n\t\treturn 0;\r\n\t}\r\n\treturn 1; \r\n}\r\nvoid fac(int n)\r\n{\r\n\tint index=0;\r\n\tint t=0;\r\n\tfor(int i=0;i<6542;i++)\r\n\t{\r\n\t\tif(a[index]>n)\r\n\t\tbreak;\t\r\n\t\tif(n%a[index]==0)\r\n\t\t{\r\n\t\t\tn/=a[index];\r\n\t\t\tif(t==0)\r\n\t\t\t{\r\n\t\t\t\tprintf(\"%d\",a[index]);\r\n\t\t\t\tt++;\r\n\t\t\t}\r\n\t\t\telse\r\n\t\t\t\tprintf(\"*%d\",a[index]);\t\r\n\t\t}\t\t\r\n\t\telse\r\n\t\t\tindex++;\r\n\t}\r\n\tif(t==0)\r\n\tprintf(\"%d\",n);\r\n\tprintf(\"\\n\");\r\n}\r\nint main()\r\n{\r\n\tint n=0;\r\n\tfor(int i=1;i<65535;i++)\r\n\t{\r\n\t\tif(isPrime(i))\r\n\t\t{\r\n\t\t\ta[n]=i;\r\n\t\t\tn++;\r\n\t\t}\r\n\t}\r\n\tint m;\r\n\tint num;\r\n\tscanf(\"%d\",&m);\r\n\twhile(m>0)\r\n\t{\r\n\t\tscanf(\"%d\",&num);\r\n\t\tfac(num);\t\r\n\t\tm--;\r\n\t}\r\n\treturn 0;\r\n}"
  },
  "1142": {
    "sid": 2479958,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<math.h>\r\nint isPrime (int n) {\r\n\tif (n < 2) return 0; \r\n\tif (n == 2) return 1; \r\n\tif (n % 2 == 0) return 0;\r\n\tint sq = sqrt(n);\r\n\tfor (int i = 3; i <= sq; i += 2) {\r\n\t\tif (n % i == 0) \r\n\t\treturn 0;\r\n\t}\r\n\treturn 1; \r\n}\r\nint duichen(int n)\r\n{\r\n\tint temp = n,m=0;\r\n    if(n<10)\r\n        return 0;\r\n\twhile (temp){\r\n\t\tm = m*10+temp%10;\r\n\t\ttemp/=10;\r\n\t}\r\n\treturn m == n;\r\n}\r\nint judge(int n)\r\n{\r\n\treturn duichen(n)&&isPrime(n);\r\n}\r\nint main()\r\n{\r\n\tint n;\r\n\twhile(scanf(\"%d\",&n)!=EOF)\r\n\t{\r\n\t\tif(judge(n))\r\n\t\t\tprintf(\"Yes\\n\");\r\n\t\telse\r\n\t\t\tprintf(\"No\\n\");\r\n\t}\r\n}"
  },
  "2649": {
    "sid": 2479956,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#define MaxSize 1000\r\ntypedef struct {\r\n    int data[MaxSize];\r\n    int length;\r\n}LNode;\r\nint main()\r\n{\r\n    LNode list;\r\n    list.length=0;\r\n    int n;\r\n    while(scanf(\"%d\",&n)!=EOF){\r\n        if(n==0)\r\n            break;\r\n        list.data[list.length]=n;\r\n        list.length++;\r\n    }\r\n    while(list.length>0){\r\n        printf(\"%d \",list.data[list.length-1]);\r\n        list.length--;\r\n    }\r\n}"
  },
  "2670": {
    "sid": 2479955,
    "code": "C++",
    "content": "#include <stdio.h>\r\nint sum = 0;\r\nvoid fac(int inStack, int wait, int out, int num)\r\n{\r\n    if(out==num)\r\n        sum++;\r\n    else{\r\n        if(inStack>0)\r\n            fac(inStack-1, wait, out+1, num);\r\n        if(wait>0)\r\n            fac(inStack+1, wait-1, out, num);\r\n    }\r\n}\r\nint main()\r\n{\r\n    int n;\r\n    scanf(\"%d\",&n);\r\n    fac(0, n, 0, n);\r\n    printf (\"%d\\n\", sum);\r\n    return 0;\r\n}"
  },
  "2655": {
    "sid": 2479954,
    "code": "C++",
    "content": "#include<stdio.h>\r\n#include \"stdlib.h\"\r\ntypedef struct Node{\r\n    int data;\r\n    struct Node *next;\r\n}*LinkList,LNode;\r\nLinkList createList()\r\n{\r\n    LinkList list=(LinkList) malloc(sizeof (LinkList));\r\n    list->data=1;\r\n    list->next=NULL;\r\n    return list;\r\n}\r\nLinkList createNode(int data){\r\n    LinkList list=(LinkList) malloc(sizeof (LinkList));\r\n    list->data=data;\r\n    list->next=NULL;\r\n    return list;\r\n}\r\nvoid addNode(LinkList list,int data){\r\n    LinkList Node= createNode(data);\r\n    Node->next=list->next;\r\n    list->next=Node;\r\n}\r\n/*void printList(LinkList list){\r\n    LinkList posNode=list;\r\n    while(posNode!=NULL){\r\n        printf(\"%d \",posNode->data);\r\n        posNode=posNode->next;\r\n    }\r\n}*/\r\nvoid loop(LinkList list){\r\n    LinkList posNode=list;\r\n    while(posNode->next!=NULL){\r\n        posNode=posNode->next;\r\n    }\r\n    posNode->next=list;\r\n}\r\nvoid deleteNode(LinkList list,int n,int m){\r\n    LinkList posNode=list;\r\n    LinkList front;\r\n    LinkList deleteNode;\r\n    for(int i=0;i<n-1;i++){\r\n        for(int j=1;j<m;j++){\r\n            front=posNode;\r\n            posNode=posNode->next;\r\n        }\r\n        front->next=posNode->next;\r\n        free(posNode);\r\n        posNode=front->next;\r\n    }\r\n    printf(\"%d\",posNode->data);\r\n}\r\nint main()\r\n{\r\n    int n,m;\r\n    LinkList list=createList();\r\n    scanf(\"%d%d\",&n,&m);\r\n    for(int i=n;i>=2;i--){\r\n        addNode(list,i);\r\n    }\r\n    loop(list);\r\n    if(m>1)\r\n        deleteNode(list,n,m);\r\n    else\r\n        printf(\"%d\",n);\r\n    return 0;\r\n}\r\n"
  },
  "1219": {
    "sid": 2479953,
    "code": "C++",
    "content": "#include<stdio.h>\r\nint main()\r\n{\r\n    int x,y;\r\n    int m,n;\r\n    int t;\r\n    while(scanf(\"%d%d\",&m,&n)!=EOF)\r\n    {\r\n\r\n        if(m>n){\r\n            t=m;\r\n            m=n;\r\n            n=t;\r\n        }\r\n        int i;\r\n        int ou=0;\r\n        int ji=0;\r\n        for(i=m;i<=n;i++)\r\n        {\r\n            if(i%2==1)\r\n            {\r\n                ji=ji+i*i*i;\r\n            }\r\n            else\r\n            {\r\n                ou=ou+i*i;\r\n            }\r\n        }\r\n        printf(\"%d %d\\n\",ou,ji);\r\n    }\r\n}"
  },
  "2699": {
    "sid": 2479952,
    "code": "C",
    "content": "#include<stdio.h>\r\n#include<string.h>\r\nint main(){\r\n    char a[1000];\r\n    char b[1000];\r\n    gets(a);\r\n    gets(b);\r\n    int x=0,y;\r\n    int i,j;\r\n    for(i=0;i< strlen(a);i++){\r\n        y=i;\r\n        for(j=0;j< strlen(b);j++){\r\n            if(b[j]!=a[y]){\r\n                break;\r\n            }\r\n            y++;\r\n        }\r\n        if(j== strlen(b)){\r\n            x++;\r\n            break;\r\n        }\r\n    }\r\n    if(x>0){\r\n        printf(\"%d %d\",i+1,i+1);\r\n    }else{\r\n        printf(\"0\");\r\n    }\r\n}"
  },
  "2013": {
    "sid": 2479951,
    "code": "C",
    "content": "#include<stdio.h>\r\n#define max 1000\r\nchar a[max];\r\nchar b[max];\r\nint ii=0;\r\nvoid fac1(int index){\r\n    if(b[index-1]=='#')\r\n        return;\r\n    printf(\"%c\",b[index-1]);\r\n    fac1(2*index);\r\n    fac1(2*index+1);\r\n}\r\nvoid fac2(int index){\r\n    if(b[index-1]=='#')\r\n        return;\r\n    fac2(2*index);\r\n    printf(\"%c\",b[index-1]);\r\n    fac2(2*index+1);\r\n}\r\nvoid fac3(int index){\r\n    if(b[index-1]=='#')\r\n        return;\r\n    fac3(2*index);\r\n    fac3(2*index+1);\r\n    printf(\"%c\",b[index-1]);\r\n}\r\nvoid f(int index){\r\n    if(a[ii]=='#'||a[ii]==NULL){\r\n        ii++;\r\n        return;\r\n    }\r\n    b[index-1]=a[ii++];\r\n    f(index*2);\r\n    f(index*2+1);\r\n}\r\nint main(){\r\n    for(int i=0;i<max;i++){\r\n        b[i]='#';\r\n    }\r\n    gets(a);\r\n    f(1);\r\n    fac1(1);\r\n    printf(\"\\n\");\r\n    fac2(1);\r\n    printf(\"\\n\");\r\n    fac3(1);\r\n}"
  },
  "2756": {
    "sid": 2479950,
    "code": "Java",
    "content": "class Main{\r\n        public static void main(String[] args)\r\n        {\r\n            \r\n        }\r\n}"
  },
  "3716": {
    "sid": 2479949,
    "code": "C",
    "content": "#include <stdio.h>\r\ntypedef struct Student\r\n{\r\n    int id;\r\n    char name[20];\r\n    struct Student *next;\r\n}STU;\r\n\r\nint main()\r\n{\r\n    STU stu[4];\r\n    int i = 0,index;\r\n    STU *head = &stu[0];\r\n    STU *p;\r\n    while(i<4)\r\n    {\r\n        scanf(\"%d,%s\", &stu[i].id, stu[i].name);\r\n        if(i < 2)\r\n            stu[i].next = &stu[i+1];\r\n        else\r\n            stu[i].next = NULL;\r\n        i++;\r\n    }\r\n    scanf(\"%d\",&index);\r\n\r\n    index++;\r\n    if(index==0){\r\n        stu[3].next=head;\r\n        p=&stu[3];\r\n    }\r\n    else{\r\n        STU *headFront;\r\n        while(index){\r\n            headFront=head;\r\n            head=head->next;\r\n            index--;\r\n        }\r\n        headFront->next=&stu[3];\r\n        stu[3].next=head;\r\n        p=&stu[0];\r\n    }\r\n\r\n    while(p!=NULL)\r\n    {\r\n        printf(\"%d,%s.\", p->id, p->name);\r\n        p = p->next;\r\n    }\r\n}"
  },
  "2789": {
    "sid": 2479948,
    "code": "Java",
    "content": "class Main{\r\n        public static void main(String[] args)\r\n        {\r\n            \r\n        }\r\n}"
  }
}