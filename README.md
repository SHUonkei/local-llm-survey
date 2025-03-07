# local llm survey
localで動くllmの動かし方を追加していきます。

## LLM
apiとして叩くなら以下で十分そう. 

ollama[https://ollama.com/]
上記サイトでダウンロード.

以下が動くはず．初回はモデルのダウンロードから始まるため時間がかかる．

```console
ollama run llama3.2
```

日本語ようにFine-Tuning したものはHuggingfaceからダウンロードできる。(koyama laptopではメモリが足りず検証できていない)
```console
ollama run hf.co/grapevine-AI/DeepSeek-R1-Distill-Qwen-32B-Japanese-GGUF
```

以下でOllama Pythonをダウンロード可能
```console
pip install -r requirements.txt
```

### Sample code
以下でurl先のweb page を要約してくれる. sample code.

```console
python main.py [web page url]
```
