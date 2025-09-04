module Jekyll
  class GitLastModified < Generator
    priority :highest

    def generate(site)
      return if site.config['skip_git_last_modified']

      site.pages.each do |page|
        next unless page.path.end_with?('.md')
        next if page.path == 'index.md'
        
        # Get git dates for the file (including renames/moves)
        dates = get_git_dates(page.path)
        page.data['git_published'] = dates[:published]
        page.data['git_last_modified'] = dates[:updated]
      end

      # Also process collection documents
      site.collections.each do |name, collection|
        collection.docs.each do |doc|
          next unless doc.path.end_with?('.md')
          
          # Get relative path from site root
          rel_path = doc.path.sub("#{site.source}/", "")
          
          dates = get_git_dates(rel_path)
          doc.data['git_published'] = dates[:published]
          doc.data['git_last_modified'] = dates[:updated]
        end
      end
    end

    private

    def get_git_dates(file_path)
      first_commit = `git log --follow --format="%at" --reverse -- "#{file_path}" 2>/dev/null | head -1`.strip
      
      last_commit = `git log --follow --format="%at" -1 -- "#{file_path}" 2>/dev/null`.strip

      if first_commit.empty? || last_commit.empty?
        file_time = File.mtime(File.join(Jekyll.sites.first.source, file_path)) rescue Time.now
        return { published: file_time, updated: file_time }
      else
        return { 
          published: Time.at(first_commit.to_i), 
          updated: Time.at(last_commit.to_i) 
        }
      end
    end
  end
end