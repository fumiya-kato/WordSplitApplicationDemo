import tkinter
import MeCab
import unidic


class Application(tkinter.Frame):
    # コンストラクタ
    def __init__(self, root):
        super().__init__(root, width=380, height=300, borderwidth=4)
        self.message = None
        self.text_box = None
        """
        self.file_name = 'app_data.txt'
        self.data = None
        """
        self.root = root
        self.pack()
        self.pack_propagate(False)
        self.create_widgets()

    # 項目作成
    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
        # テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 300
        self.text_box.pack()
        # テキスト送信
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()
        # 画面出力
        self.message = tkinter.Message(self)
        self.message.pack()
        '''
        if self.message != None:
            # 保存ボタン
            save_btn = tkinter.Button(self)
            save_btn['text'] = '保存'
            save_btn['command'] = self.save_handler
            save_btn.pack()
        
        if self.data != None:
            # 読み込みデータ
            self.data = tkinter.Message(self)
            self.data.pack()
        '''

    # テキスト読み込み
    def input_handler(self):
        text = self.text_box.get()
        wakati = MeCab.Tagger('-Owakati')
        wakati_text = wakati.parse(text)
        wakati_text = wakati_text.replace('。', ' ')
        wakati_text = wakati_text.replace('、', ' ')

        self.message['text'] = wakati_text
    '''
    # テキスト保存
    def save_handler(self):
        with open(file_name, 'a', encoding='utf-8')as file:
            messageList = message.split()
            for m in messageList:
                file.write("'"+m+"' ", end=' ') 
        print('保存完了')
    
    # テキスト読み込み
    def read_handler(self):
        with open(file_name, 'r', encoding='utf-8')as file:
            read_data = file.read()
            data += read_data
    '''


root = tkinter.Tk()
root.title('文章分割アプリ')
# アプリ画面サイズ
root.geometry(newGeometry='400x600')
# 処理内容
app = Application(root=root)
app.mainloop()
