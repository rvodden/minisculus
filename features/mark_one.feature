Feature: The MARK I Encoder.
    Our crack team of undercover operatives, the Special Secret People of Awesomeness (SSPA), have intercepted plans for an enemy message encoding machine known as the MARK I. The early prototype has been trial tested on the Western front to call in artillery strikes with great success, leading to many causalities on our side. Your mission is to create a computerized version of the MARK I.

    The plans captured show the MARK I as being a very simple device. The operator sets an encoder wheel to a value between 0 and 9 as pre-determined by standard operating protocols. They then type on a keyboard and the resulting encoded character is sent to the field, which is then decoded and the commands are carried out.

    The keyboard has the following set of characters (assuming a zero-based index), which are used for both the input and output messages.


    [
      "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
      "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
      ".", ",", "?", "!", "'", "\"", " "
    ]

    The MARK I functions by shifting the input character by the number shown on the wheel. Therefore, with a wheel setting of 5, an input character of 'a' will result in an encoded character of 'f', 'c' becomes 'h', and so forth. If the new index falls off the end of the set of characters, then it simply loops back to the beginning (and vice versa).

    You will need to encode the words 'Strong NE Winds!' using your virtual MARK I device set at wheel position 6 and send it back to via JSON to allow you to move on to the next question.

    Scenario Outline: Wheel settings should cause characters to be encoded correctly.
        Given a mark one machine with its wheel set to 5
        When the string '<plain text>' is encoded
        Then the string '<cypher text>' is returned.

        Examples:
            | plain text | cypher text |
            | a          | f           |
            | c          | h           |
