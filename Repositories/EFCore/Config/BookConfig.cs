﻿using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Entities.Models;

namespace Repositories.EFCore.Config
{
    public class BookConfig : IEntityTypeConfiguration<Book>
    {
        public void Configure(EntityTypeBuilder<Book> builder)
        {
            builder.HasData(
                new Book { Id = 1, Title = "Karagöz ve Hacivat", Price = 75 },
                new Book { Id = 2, Title = "Nutuk", Price = 275 },
                new Book { Id = 3, Title = "Kara Tren", Price = 375 }
            );
        }
    }
}
