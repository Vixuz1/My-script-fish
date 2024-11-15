
while true do
    -- Функция для автоматической ловли рыбы
    local function fish()
        -- Найти объект для ловли рыбы
        local fishingSpot = game.Workspace:FindFirstChild("FishingSpot")
        if fishingSpot then
            -- Переместиться к месту ловли рыбы
            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = fishingSpot.CFrame
            -- Начать ловить рыбу (клик)
            local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("FishingRod")
            if tool then
                game.Players.LocalPlayer.Character.Humanoid:EquipTool(tool)
                tool:Activate()
                wait(5) -- ожидание окончания ловли рыбы
                tool:Deactivate()
            end
        end
    end
    local function buyCrabTrap()
        local shop = game.Workspace:FindFirstChild("Shop")
        if shop then
            -- Переместиться в магазин
            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = shop.CFrame
            -- Покупка ловушки для крабов
            local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("Wallet")
            if tool then
                game.Players.LocalPlayer.Character.Humanoid:EquipTool(tool)
                tool:Activate()
                wait(2) -- ожидание завершения покупки
                tool:Deactivate()
            end
        end
    end
    local function setCrabTrap()
        local trapLocation = game.Workspace:FindFirstChild("TrapSpot")
        if trapLocation then
            -- Переместиться к месту установки ловушки
            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = trapLocation.CFrame
            -- Установить ловушку
            local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("CrabTrap")
            if tool then
                game.Players.LocalPlayer.Character.Humanoid:EquipTool(tool)
                tool:Activate()
                wait(3) -- ожидание установки ловушки
                tool:Deactivate()
            end
        end
    end

    fish() -- Автоматически ловить рыбу
    wait(10) -- Ожидание перед покупкой ловушки (опционально)
    buyCrabTrap() -- Купить ловушку для крабов
    wait(2) -- Ожидание перед установкой ловушки (опционально)
    setCrabTrap() -- Установить ловушку для крабов
    wait(60) -- Ожидание перед следующим циклом
end