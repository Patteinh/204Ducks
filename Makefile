##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## Makefile
##

NAME		= 	204ducks

SRC_DIR		= 	./src/

TEST_DIR	= 	./tests/

all: $(NAME)

$(NAME):
	@cp $(SRC_DIR)main.py $@
	@chmod +x $@

tests_run:
	make -C $(TEST_DIR)

clean:
	make clean -C $(TEST_DIR)
	$(RM) -r $(SRC_DIR)__pycache__

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all tests_run clean fclean
