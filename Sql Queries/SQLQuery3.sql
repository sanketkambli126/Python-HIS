USE [HIS]
GO
INSERT INTO dbo.Policy
(
    --policy_id - column value is auto-generated
    created_date,
    modified_date,
    is_renewed,
    total_amount_canclaim,
    issued_date,
    inception_date,
    expiry_date,
    member_id_id,
    plan_id_id
)
VALUES
(
    -- policy_id - int
    DATEADD(DD,-730,GETDATE()), -- created_date - datetime2
    NULL, -- modified_date - datetime2
    0, -- is_renewed - bit
    1000000, -- total_amount_canclaim - numeric
    GETDATE(), -- issued_date - datetime2
    GETDATE(), -- inception_date - datetime2
    CAST(DATEADD(DD,365,GETDATE()) AS DATETIME), -- expiry_date - datetime2
    5, -- member_id_id - int
    1 -- plan_id_id - int
)

GO
INSERT INTO dbo.Policy
(
    --policy_id - column value is auto-generated
    created_date,
    modified_date,
    is_renewed,
    total_amount_canclaim,
    issued_date,
    inception_date,
    expiry_date,
    member_id_id,
    plan_id_id
)
VALUES
(
    -- policy_id - int
    CAST(DATEADD(DD,366,GETDATE()) AS DATETIME), -- created_date - datetime2
    NULL, -- modified_date - datetime2
    1, -- is_renewed - bit
    1250000, -- total_amount_canclaim - numeric
    CAST(DATEADD(DD,361,GETDATE()) AS DATETIME), -- issued_date - datetime2
    GETDATE(), -- inception_date - datetime2
    CAST(DATEADD(DD,730,GETDATE()) AS DATETIME), -- expiry_date - datetime2
    5, -- member_id_id - int
    1 -- plan_id_id - int
)

GO
INSERT INTO dbo.Policy
(
    --policy_id - column value is auto-generated
    created_date,
    modified_date,
    is_renewed,
    total_amount_canclaim,
    issued_date,
    inception_date,
    expiry_date,
    member_id_id,
    plan_id_id
)
VALUES
(
    -- policy_id - int
    -- policy_id - int
    CAST(DATEADD(DD,731,GETDATE()) AS DATETIME), -- created_date - datetime2
    NULL, -- modified_date - datetime2
    1, -- is_renewed - bit
    1500000, -- total_amount_canclaim - numeric
    CAST(DATEADD(DD,724,GETDATE()) AS DATETIME), -- issued_date - datetime2
    GETDATE(), -- inception_date - datetime2
    CAST(DATEADD(DD,1095,GETDATE()) AS DATETIME), -- expiry_date - datetime2
    5, -- member_id_id - int
    1 -- plan_id_id - int
)
GO
INSERT INTO dbo.Policy
(
    --policy_id - column value is auto-generated
    created_date,
    modified_date,
    is_renewed,
    total_amount_canclaim,
    issued_date,
    inception_date,
    expiry_date,
    member_id_id,
    plan_id_id
)
VALUES
(
    -- policy_id - int
    -- policy_id - int
    CAST(DATEADD(DD,731,GETDATE()) AS DATETIME), -- created_date - datetime2
    NULL, -- modified_date - datetime2
    1, -- is_renewed - bit
    1500000, -- total_amount_canclaim - numeric
    CAST(DATEADD(DD,724,GETDATE()) AS DATETIME), -- issued_date - datetime2
    GETDATE(), -- inception_date - datetime2
    CAST(DATEADD(DD,1095,GETDATE()) AS DATETIME), -- expiry_date - datetime2
    5, -- member_id_id - int
    1 -- plan_id_id - int
)



SELECT * FROM dbo.Policy p