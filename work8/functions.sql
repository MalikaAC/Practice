-- Function: search contacts by pattern (name or phone)
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE username ILIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- Function: pagination (LIMIT + OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_page(lim INT, offs INT)
RETURNS TABLE(username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;