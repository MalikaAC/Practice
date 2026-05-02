CREATE OR REPLACE PROCEDURE move_to_group(
    p_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    cid INT;
    gid INT;
BEGIN
    -- найти контакт
    SELECT id INTO cid FROM contacts WHERE username = p_name;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    -- найти или создать группу
    SELECT id INTO gid FROM groups WHERE name = p_group_name;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group_name)
        RETURNING id INTO gid;
    END IF;

    -- обновить контакт
    UPDATE contacts
    SET group_id = gid
    WHERE id = cid;
END;
$$;