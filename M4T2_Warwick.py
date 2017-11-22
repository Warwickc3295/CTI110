# CTI-110
# M4T2 - Python Exercise
# Cameron Warwick
# 10/2/17

def main():
    # Ask the user for a string
    tag = input('Please input an HTML tag: ')
    

    #If it's one of the tags, print what the tag is and an example of it's use
    if tag == "p":
        print('<p> is the paragraph tag.')
        print('Example of use: <p>text</p>')
        
    elif tag == "h1":
        print('<h1> is used to define HTML headings, h1 defines most the important.')
        print('<h1>This is a heading</h1>')

    elif tag == "b":
        print('<b> is used to bold text')
        print('<b>This text would be bold</b>')
    
    elif tag == "div":
        print('<div> is used to help divide the HTML document in to sections')
        print('<div> Page elements would go between </div>')
        
    else:
        print('Sorry, tag not found.')


    # else print ('Tag not found')

main()

