## Regex 101

Este documento tem como propósito orientar quem não tenha muita experiência com Expressões Regulares/regex e ensinar a formular Expressões Regulares válidas.

1. **Basic**
    > **`^_`** ==> Início da linha

    > **`_$`** ==> Fim da linha
    
    > **`.`** ==> Wildcard (pode ser qualquer char)
    
    > **`_|_`** ==> Usado neste contexto **`a|b`**, serve como disjunção da captura **(`a|bc|d` ⊃ `{'bc','d','a'}`)**
    
    > **`\_`** ==> Torna as "palavras reservadas" de regex em strings normais  **(`\[` == `"["`)**
    
    > **strings** ==> Qualquer string recebida que não faça parte das "palavras reservadas" 
    
        Neste documento, todas as ocorrências do char _ deverão ser substituídas por strings ou expressões de strings, e.g. 'a?', '(?:b|c)', '[c{3,7},(\d),d{6}]', 'boas'

2. **Quantifiers** 
    
    > **`_*`** ==> 0 ou mais ocorrências de uma string **(`a*` ⊃ `{'','a','aaaaaaaa'}`)**
    
    > **`_+`** ==> 1 ou mais ocorrências de uma string **(`a*b+` ⊃ `{'b','bbb','ab','aab','aaabb'}`)**
    
    > **`_?`** ==> 0 ou 1 ocorrência de uma string **(`c?` ⊃ `{'','c'}`)**
    
    > **`_{...}`** ==> Quantia específica de ocorrências de uma string **(`d{4}` = `'dddd'`)**
    
    > **`_{...,}`** ==> Quantia mínima de ocorrências de uma string **(`d{4,}` ⊃ `{'dddd', 'ddddddd'}`)**
    
    > **`_{..., ...}`** ==> Intervalo da quantia de ocorrências de uma string **(`d{2,4}` ⊃ `{'dd','ddd','dddd'}`)**

    Tanto o `*` como o `+` tendem a consumir mais chars do que desejado, dependendo do contexto dado (basta experimentar usar a Expressão Regular `(?:").*(?:")` num texto com mais do que 2 chars `"` para perceber que o resultado obtido difere do esperado (isto acontece pelo `*` consumir o 2º `"` em vez de parar aí 🤓))

    Para evitar isto, é normal acompanhar ambos com um `?` (e.g. `.*?`)

3. **Classes**
    
    > **`\s`** ==> Qualquer string que seja um whitespace **(`\s` ⊃ `{' ', '\t', '\n'}`)**
    
    > **`\S`** ==> Qualquer string que não seja um whitespace **(`\S` ⊅ `{' ', '\t', '\n'}`)**
    
    > **`\w`** ==> Qualquer string alfanumérica 

          \w = [A-Za-z0-9_]
          \w ⊃ {'a', 'G', '5', '_'}

    > **`\W`** ==> Qualquer string não alfanumérica 
          
          \W ≠ [A-Za-z0-9_]
          \W ⊅ {'a', 'G', '5', '_'}
    
    > **`\d`** ==> Qualquer string numérica 
        
          \d = [0-9]
          \d ⊃ {'0', '2', '5', '9'}
    
    > **`\D`** ==> Qualquer string numérica 
        
          \D ≠ [0-9]
          \D ⊅ {'0', '2', '5', '9'}

4. **Special Chars**
    
    > **`\n`** ==> Mudança de linha (clica no Enter para escrever um `'\n'` na tela)
    
    > **`\t`** ==> Tab (clica no Tab para escrever um `'\t'` na tela)
    
5. **Capture groups**
    
    > **`(_)`** ==> O grupo de captura está dentro dos parêntesis, tudo o que estiver fora não é colocado neste grupo. 

    ```py
      import re

      pat = 'a(bc)'
      text = 'abc'

      result = re.findall(pat, text)

      # result = ['bc']
    ```


    ```py
      import re

      pat = 'a(bc)|(de)'
      
      text1 = 'abc'
      text2 = 'de'
      text3 = 'dedeabcde'

      result1 = re.findall(pat, text1)
      result2 = re.findall(pat, text2)
      result3 = re.findall(pat, text3)

      # result1 = [('bc', '')]
      # result2 = [('', 'de')]
      # result3 = [('', 'de'), ('', 'de'), ('bc', ''), ('', 'de')]
    ```

    > **`(?:_)`** ==> Agrupa a expressão dentro dos parêntesis para aplicar quantificadores ou outras operações, mas não captura o conteúdo para ser retornado ou referenciado depois

    ```py
      import re

      pat = 'a(?:bc|de)'
      
      text1 = 'abc'
      text2 = 'ade'

      result1 = re.findall(pat, text1)
      result2 = re.findall(pat, text2)

      # result1 = ['abc']
      # result2 = ['ade']
    ```


    > **`[__]`** ==> Char correspondente a qualquer um dos chars especificados dentro dos parêntesis retos

          [abc6] ⊃ {'a', 'b', 'c', '6'}
          [abc6]* ⊃ {'', 'ba66', 'c6cccccc', 'a'}
    
    > **`[^__]`** ==> Char que não está especificado nos parêntesis retos

          [^abc6] ⊅ {'a', 'b', 'c', '6'}
          [^abc6] ⊃ {'z', '@', 'D', '7', ' '}

    
    > **`[_-_]`** ==> Intervalo de chars, tendo em conta a ordem da tabela ASCII

          [0-9]* ⊃ {'', '0123456789'}
          [a-z]* ⊃ {'', 'abcdefghijklmnopqrstuvwxyz'}
          [a-g1-3H-J]* ⊃ {'', 'abcdefg123HIJ'}


6. **Lookaheads**
    
    > **`(?=_)`** ==> Lookahead positivo, verifica se uma string aparece, imediatamente, após uma dada posição na string a ser analisada pelo regex, sem a adicionar ao grupo de captura

    ```py
      import re

      pat1 = 'k(?=[ab])'
      pat2 = 'X(?=string)Y'
      pat3 = '.(?=c)'
      pat4 = 'a(?=.)'
      
      text1 = 'kakbkc'
      text2 = 'este texto de input está muito XstringY bem feito'
      text3 = 'abcdecfgc'
      text4 = 'aacaeafac'
      text5 = 'aa'

      result1 = re.findall(pat1, text1)
      result2 = re.findall(pat2, text2)
      result3 = re.findall(pat3, text3)
      result4 = re.findall(pat4, text4)
      result5 = re.findall(pat4, text5)

      # result1 = ['k','k']
      # result2 = ['XY']
      # result3 = ['b','e','g']
      # result4 = ['a','a','a','a','a']
      # result5 = ['a','a']

      # a(?=.)  ==  a
    ```



    > **`(?!_)`** ==> Lookahead negativo, verifica se uma string não aparece, imediatamente, após uma dada posição na string a ser analisada pelo regex, sem a adicionar ao grupo de captura

      ```py
      import re

      pat = 'a(?!c)'
      text = 'aaca'

      result = re.findall(pat, text)    
      
      # aaca   ==>  [a]ac[a]
      # result = ['a','a']
    ```

7. Lookbehinds

    > **`(?<=_)`** ==> Lookbehind positivo, verifica se uma string aparece, imediatamente, antes de uma dada posição na string a ser analisada pelo regex, sem a adicionar ao grupo de captura

      ```py
      import re

      pat1 = '(?<=k)a'
      pat2 = '(?<=X)stringY'
      pat3 = '(?<=b)c'
      pat4 = '(?<=a).'

      text1 = 'kakbkc'
      text2 = 'este texto de input está muito XstringY bem feito'
      text3 = 'abcdecfgc'
      text4 = 'aacaeafac'

      result1 = re.findall(pat1, text1)
      result2 = re.findall(pat2, text2)
      result3 = re.findall(pat3, text3)
      result4 = re.findall(pat4, text4)

      # result1 = ['a']
      # result2 = ['stringY']
      # result3 = ['c']
      # result4 = ['c','e','f','c']
    ```

    > **`(?<!_)`** ==> Lookbehind negativo, verifica se uma string não aparece, imediatamente, antes de uma dada posição na string a ser analisada pelo regex, sem a adicionar ao grupo de captura

      ```py
      import re

      pat = '(?<!a)c'
      text = 'aaca'

      result = re.findall(pat, text)    

      # aaca   ==>  aac[a]
      # result = ['c']
    ```



Estas são algumas das operações e tokens que podem ser usados em Expressões Regulares, há mais algumas, mas para um contexto didático estes servem.

Agora, com tudo isto mencionado, só falta indicar que é possível criar Expreessões Regulares por composição, e.g.: 

1. `^a[a-z]{2,4}z$`
2. `(\w+)(?=\.)`
3. `b[a-e]*t`
4. `(foo|bar)(?!baz)`
5. `^\w{3,8}$`
6. `(?<=")[^"]*(?=")`