import asyncio

from core.models import db_helper, User, Profile, Post

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(name = username)
    session.add(user)
    await session.commit()
    print("user", user)
    return user

async def get_user_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.name == username)
    # result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    
    user: User | None = await session.scalar(stmt)
    print("found user", username,user)
    return user 

async def create_user_profile(
    session: AsyncSession, 
    user_id: int,
    first_name: str | None,
    last_name: str | None
) -> Profile:
    profile = Profile(
        user_id = user_id,
        first_name = first_name,
        last_name = last_name
    )
    session.add(profile)
    await session.commit()
    return profile
    

async def show_users_with_profiles(session: AsyncSession):
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    users = await session.scalars(stmt)
    for user in users:
        print(user)
        print(user.profile.first_name)
        
async def create_posts(
    session: AsyncSession, 
    user_id: int, 
    *post_titles: str
    ) -> list[Post]:
    posts = [Post(title = title, user_id = user_id) for title in post_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts
    
async def get_user_with_posts(
    session: AsyncSession,
):
    stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    # users = await session.scalars(stmt)
    result: Result = await session.execute(stmt)
    
    users = result.scalars()
    
    for user in users:
        print("**"*10)
        print(user)
        for post in user.posts:
            print("-", post)
            
async def get_post_with_authors(session: AsyncSession):
    stmt = select(Post).options(selectinload(Post.user)).order_by(Post.id)
    posts = await session.scalars(stmt)
    
    for post in posts:
        print("post", post)
        print(" - author", post.user)
        
async def get_user_with_posts_and_profiles(
    session: AsyncSession,
):
    stmt = select(User).options(
        joinedload(User.profile),
        selectinload(User.posts)
    ).order_by(User.id)
    # users = await session.scalars(stmt)
    
    users = await session.scalars(stmt)
    
    for user in users:
        print("**"*10)
        print(user, "Profile:",user.profile.first_name)
        for post in user.posts:
            print("-", post)
            
async def get_profiles_with_users_and_users_with_posts(session: AsyncSession):
    stmt = (
        select(Profile)
        .options(
            joinedload(Profile.user).selectinload(User.posts),
        )
        .order_by(Profile.id)
    )
    
    profiles = await session.scalars(stmt)
    
    for profile in profiles:
        print(profile.first_name, profile.user)
        print(profile.user.posts)

async def main_relations(session: AsyncSession):
    # await create_user(session = session, username = "Ivan12")
        # await create_user(session = session, username = "Sergey12")
        # user_Ivan = await get_user_username(session = session, username = "Ivan")
        # await get_user_username(session = session, username = "Ivan")
        
        # user_Sergey = await get_user_username(session = session, username = "Sergey")
        
        # user_Ivan12 = await get_user_username(session = session, username = "Ivan12")
        
        # user_Sergey12 = await get_user_username(session = session, username = "Sergey12")
        
        # await create_user_profile(
        #     session = session,
        #     user_id = user_Sergey12.id,
        #     first_name = user_Sergey12.name,
        #     last_name = user_Sergey12.name
        # )
        
        # await show_users_with_profiles(session = session)
        
        # await create_posts(
        #     session,
        #     user_Sergey12.id,
        #     "FastApi Test",
        #     "FastAPI User",
        #     "FastAPI In"

        # )
        
        # await create_posts(
        #     session,
        #     user_Sergey.id,
        #     "SQLA 3.0",
        #     "SQLA Wait",
        # )
        
        # await create_posts(
        #     session,
        #     user_Ivan12.id,
        # )
    
    
        # await get_user_with_posts(session = session)
        
        await get_post_with_authors(session = session)
        
        # await get_user_with_posts_and_profiles(session = session)
        
        # await get_profiles_with_users_and_users_with_posts(session = session)

async def demo_m2m(session: AsyncSession):
    pass

async def main():
    async with db_helper.session_factor() as session:
        await main_relations(session = session)
    
if __name__ == '__main__':
    asyncio.run(main())