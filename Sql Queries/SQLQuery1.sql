USE [HIS]
GO
INSERT INTO dbo.Member
(
    --member_id - column value is auto-generated
    member_name,
    date_of_birth,
    contact_details,
    created_date,
    modified_date
)
VALUES
(
    -- member_id - int
    N'Sanket', -- member_name - nvarchar
    '1998-06-12', -- date_of_birth - datetime2
    0, -- contact_details - int
    GETDATE(), -- created_date - datetime2
    NULL -- modified_date - datetime2

)
GO
INSERT INTO dbo.Member
(
    --member_id - column value is auto-generated
    member_name,
    date_of_birth,
    contact_details,
    created_date,
    modified_date
)
VALUES
(
    -- member_id - int
    N'Rohan', -- member_name - nvarchar
    '2000-07-09', -- date_of_birth - datetime2
    0, -- contact_details - int
    GETDATE(), -- created_date - datetime2
    NULL -- modified_date - datetime2

)

