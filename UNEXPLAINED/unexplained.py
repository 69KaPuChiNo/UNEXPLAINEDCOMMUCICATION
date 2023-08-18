import base64
import time

english_to_georgian = {
    'a': 'ქ', 'b': 'წ', 'c': 'ე', 'd': 'რ', 'e': 'ყ', 'f': 'უ', 'g': 'ი', 'h': 'ო',
    'i': 'ა', 'j': 'ს', 'k': 'დ', 'l': 'ფ', 'm': 'გ', 'n': 'ჰ', 'o': 'ჯ', 'p': 'კ',
    'q': 'ლ', 'r': 'ზ', 'ხ': 'ც', 't': 'ვ', 'u': 'ბ', 'v': 'ნ', 'w': 'მ', 'x': 'ხ',
    'y': 'ტ', 'z': 'პ',
}

def encode_english_to_georgian(text):
    georgian_text = ''.join([english_to_georgian.get(c, c) for c in text.lower()])
    return georgian_text

def encode_georgian_to_base64(georgian_text):
    encoded_bytes = georgian_text.encode("utf-8")
    base64_encoded = base64.b64encode(encoded_bytes).decode("utf-8")
    return base64_encoded

def decode_base64_to_georgian(base64_text):
    base64_decoded = base64.b64decode(base64_text.encode("utf-8"))
    georgian_text = base64_decoded.decode("utf-8")
    return georgian_text

def decode_georgian_to_english(georgian_text):
    english_text = ''.join([next((k for k, v in english_to_georgian.items() if v == c), c) for c in georgian_text])
    return english_text

def display_anonymous_banner():
    banner = """
                                                                                                 --           +:                                          
                                                                                            +@+ .       ..*@+                                         
                                                                                           -@*-@@.  .  .@@:#@.                                        
                                                                                           *@-%@- -@@@: +@* @-                                        
                                                                                           =@=#@+ :%@%. *@**@:                                        
                                                                                            #@+%#  *@* .@*+@#                                         
             ..      ...      ...       .......      ..       ..        .:--:.   ..        ..=+    *@*   .#*.       ..      .:-+++-:                  
             @@    .#@*.     +@@@.      @@%###@%+   =@*       @@-    -#@%#####+  @@*       @@      *@*    *@@-      #@-   -+%*. *.=%++.               
             @@   =@%-      .@@+@#      @@=    *@+  =@*       @@-   #@*.         @@*       @@      *@*    *@%@+     *@- .#*+#--+%--#%+@=              
             @@ -@@-        #@: %@-     @@=    :@*  =@*       @@-  @@=           @@*       @@      *@*    *@-+@%.   *@-.%. #    *   :* ==             
             @@#@@#        +@+   %@     @@*---*@@.  =@*       @@- -@@            @@@@@@@@@@@@      *@*    *@- :@@=  *@--#+#%++++%++++@++@             
             @@=.=@#      :@@*+++%@#    @@#+++=.    =@*       @@- :@@.           @@+       @@      *@*    *@-  .%@+ *@--* -*   :*    #  %             
             @@   -@@-    %@*-----@@=   @@=         .@#      .@@   #@*           @@*       @@      *@*    *@-    #@+*@- #-.#...-#...+*.#-             
             @@    :%@+  *@%      -@@.  @@=          +@*.   :%@+    +@%+:    ..  @@*      :@@      *@*    *@-     *@@@-  +#+@--+#..+#-#:              
             **      +*+:**        =*+  **-           -+#%%#*=       .=**%%%#*-  **-       #*      =*=    =*:      -**:    =*#+*#=##=-                

    """
    for char in banner:
        print(char, end='', flush=True)
        time.sleep(0.0001)  
    print("ENCODE AND DECODE TOOL (BE INEXPLICABLE)")

def main():
    display_anonymous_banner()
    
    while True:
        choice = input("Do you want to encode or decode? (e/d): ").lower()
        
        if choice == 'e':
            input_text = input("Enter the English text you want to encode: ")
            georgian_text = encode_english_to_georgian(input_text)
            base64_encoded = encode_georgian_to_base64(georgian_text)
            print("Encoded Result:", base64_encoded)
        
        elif choice == 'd':
            input_text = input("Enter the base64-encoded text you want to decode: ")
            georgian_text = decode_base64_to_georgian(input_text)
            english_text = decode_georgian_to_english(georgian_text)
            print("Decoded Result (English):", english_text)
        
        else:
            print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")

        again = input("Do you want to continue? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
