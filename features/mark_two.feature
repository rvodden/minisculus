Feature: The MARK II machine.
    The SSPA has had another success! During a raid on a captured communication outpost in Prague, an updated version of the encoding machine has been obtained. The MARK II has a design evolved from the MARK I in that it still has a letter shifting first wheel, however, a second wheel has been added to further complicate the encoded message. The MARK II's second wheel is set the same way as the first, e.g. a 0-9 setting. The difference is that the second wheel shifts the characters in a REVERSE direction TWO TIMES the number shown on the wheel's setting. This means, a MARK II machine with wheel settings of 2 [First Wheel], 5 [Second Wheel] and input characters of 'abc' will result in an output of 'STU'

    Your task is to update your machine to add the second wheel. Make haste! Our anti-fascist forces are relying on you!

    JSON question... using the wheel settings of 9,3 what would the encoded message be for the input 'The Desert Fox will move 30 tanks to Calais at dawn'?


    Scenario Outline: Wheel settings should cause characters to be encoded correctly.
        Given a mark two machine with its wheels set to 2 and 5
        When the string '<plain text>' is encoded
        Then the string '<cypher text>' is returned.

        Examples:
            | plain text | cypher text |
            | abc        | STU         |
