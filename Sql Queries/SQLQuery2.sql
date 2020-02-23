USE [HIS]
GO
INSERT INTO dbo.Company
(
    --company_id - column value is auto-generated
    company_name,
    company_email,
    created_date,
    startd_ate
)
VALUES
(
    -- company_id - int
    N'HDFC', -- company_name - nvarchar
    N'hr@hdfc.com', -- company_email - nvarchar
    GETDATE(), -- created_date - datetime2
    GETDATE() -- startd_ate - datetime2
)

GO
INSERT INTO dbo.Plans
(
    --plan_id - column value is auto-generated
    name,
    premium,
    sum_assured,
    created_date,
    is_active,
    company_id_id
)
VALUES
(
    -- plan_id - int
    N'Base Plan', -- name - nvarchar
    10000, -- premium - numeric
   1000000, -- sum_assured - numeric
    GETDATE(), -- created_date - datetime2
    1, -- is_active - bit
    1 -- company_id_id - int
)
GO
INSERT INTO dbo.Plans
(
    --plan_id - column value is auto-generated
    name,
    premium,
    sum_assured,
    created_date,
    is_active,
    company_id_id
)
VALUES
(
    -- plan_id - int
    N'Top Up', -- name - nvarchar
    4000, -- premium - numeric
   1000000, -- sum_assured - numeric
    GETDATE(), -- created_date - datetime2
    1, -- is_active - bit
    1 -- company_id_id - int
)
GO
INSERT INTO dbo.Plans
(
    --plan_id - column value is auto-generated
    name,
    premium,
    sum_assured,
    created_date,
    is_active,
    company_id_id
)
VALUES
(
    -- plan_id - int
    N'Super Top Up', -- name - nvarchar
    5000, -- premium - numeric
   1000000, -- sum_assured - numeric
    GETDATE(), -- created_date - datetime2
    1, -- is_active - bit
    1 -- company_id_id - int
)


