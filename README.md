# KaleidoKeyFinderSwitch
Find the key of Kaleido ADV Workshop games on Switch.  
此工具用于寻找Switch平台的Kaleido ADV Workshop引擎的游戏的密钥。  
测试时使用了 _ANONYMOUS;CODE(JP)_，_五等分の花嫁∬～夏の思い出も五等分～_，_映画 五等分の花嫁～君と過ごした五つの思い出～_ 三个游戏。  
Switch平台的Kaleido ADV Workshop引擎的游戏的密钥存储在exefs/main文件中，可以用[Ryujinx](https://github.com/Ryujinx/Ryujinx)提取该文件。  
但其在文件中的位置很不固定，密钥的内容也很随机，没有什么好方法去找它。  
在以上三个游戏中，密钥的共同点只有：  
 1. 13个字符长。尽管其他平台的游戏有特殊情况。  
 2. 该字符串前一字节为\\x00。  
 3. 总是既有数字又有字母，且不含数字和大小写字母以外的字符。  
 4. 总是没有任何含义，无法提取出单词。  

此段代码用穷举的方法，列举出所有\\x00后紧跟13个数字或字母的字符串，并优先标记出其中同时包含数字和字母的组合，再由用户手动筛选或逐个测试。  
以 _ANONYMOUS;CODE(JP)_ 为例，最终可提取出53个符合规则的字符串，并优先标记了其中的8个。  
  
很遗憾，此段代码在针对 _ANONYMOUS;CODE(ENG)_ 测试时无法找到密钥，因为密钥的最后一位字符似乎与后续数据重合而变成了数字、字母以外的字符。幸好该密钥和Steam版相同才得以定位这个问题。代码修改为了只寻找连续的12个字符，但输出时仍尝试输出13个字符。  
现在以 _ANONYMOUS;CODE(JP)_ 为例，最终可提取出71个可能符合规则的字符串，并优先标记了其中的8个。  
  
2024.3.27 [FreeMote#124](https://github.com/UlyssesWu/FreeMote/issues/124) 现在密钥中可能出现标点符号。  