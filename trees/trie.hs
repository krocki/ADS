-- @Author: krocki
-- @Date:   2017-01-11 16:10:29
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-12 16:14:33

-- We're going to make our own Contacts
-- application! The application must perform two
-- types of operations:

-- add name, where  is a string denoting a contact
-- name. This must store  as a new contact in the
-- application. find partial, where  is a string
-- denoting a partial name to search the
-- application for. It must count the number of
-- contacts starting with  and print the count on
-- a new line.

data Trie = Node Char [Trie] deriving (Eq, Show)

-- returns the modified list of Tries
insert (x:xs) [] = [Node x (insert xs [])]
insert [] [] = [(Node '*' [])]
insert [] ((Node c' l'):ls) = ((Node c' (insert "*" l')):ls)
insert xx@(x:xs) (l@(Node c' l'):ls)
                        | x == c' = ((Node c' (insert xs l')):ls)
                        | x /= c' = (l:insert xx ls)

add :: String -> Trie -> Trie
add xx (Node c l) = (Node c (insert xx l))

main = do
    -- root is marked by symbol "#", word ending is marked by "*"
    let root = add "cars" (add "cat" (add "car" (Node '#' [])))
    print root
    -- == Node '#' 
        -- [Node 'c' 
                -- [Node 'a' 
                    -- [Node 'r' 
                        -- [Node '*' [], Node 's' 
                                -- [Node '*' []
                                -- ]
                        -- ],
                    -- Node 't' 
                        -- [Node '*' []
                        -- ]
                    -- ]
                -- ]
        -- ]

