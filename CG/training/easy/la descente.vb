Module Player
' Auto-generated code below aims at helping you parse
' the standard input according to the problem statement.

    Sub Main ()
        
        Dim max as integer, index as integer
        While True
            max = 0
            index = 0
            For i as Integer = 0 To 7
                Dim mountainH as Integer
                mountainH = Console.ReadLine() ' represents the height of one mountain, from 9 to 0.
                if mountainH > max then
                    max = mountainH
                    index = i
                end if
            Next i

            ' Write an action using Console.WriteLine()
            ' To debug: Console.Error.WriteLine("Debug messages...")

            Console.WriteLine(index) ' The number of the mountain to fire on.
        End While
    End Sub
End Module