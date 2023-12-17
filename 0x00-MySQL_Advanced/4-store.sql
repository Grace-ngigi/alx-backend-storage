-- SQL script that creates a trigger that decreases the quantity of an
-- item after adding a new order.
-- Quantity in the table items can be negative.

DELIMITER $$

USE `holberton`$$

CREATE DEFINER=`root`@`localhost`
TRIGGER decr_items 
AFTER INSERT ON `holberton`.`orders`
FOR EACH ROW
	BEGIN
	UPDATE `holberton`.`items` SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
END$$

DELIMITER ;
