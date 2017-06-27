Module Solution
' Auto-generated code below aims at helping you parse
' the standard input according to the problem statement.

    Sub Main ()
        
        Dim N as Integer
        N = Console.ReadLine()
        Dim list_Array(N) As Integer
        dim diff as Integer, min_diff as Integer
        min_diff = 1000
        
        For i as Integer = 0 To N-1
            Dim Pi as Integer
            Pi = Console.ReadLine()
            list_Array(i+1) = Pi
        Next i
        
        Array.Sort(list_Array)
        
        For i as Integer = 1 To N-1
            diff = Math.Abs(list_Array(i)-list_Array(i+1))
            if diff < min_diff then
                min_diff = diff
            end if
            'Console.Error.WriteLine(list_Array(i))
        Next i
    
        ' Write an action using Console.WriteLine()
        ' To debug: Console.Error.WriteLine("Debug messages...")

        Console.WriteLine(min_diff)
    End Sub
End Module